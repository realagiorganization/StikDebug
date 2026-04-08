from dataclasses import dataclass, field
from typing import List, Dict, Optional
from behave import given, when, then


@dataclass
class Device:
    name: str
    os_version: str
    trusted: bool = False
    connected: bool = False


@dataclass
class StikDebugApp:
    device: Optional[Device] = None
    jit_enabled_bundles: set[str] = field(default_factory=set)
    logs: List[str] = field(default_factory=list)
    mini_tool_catalog: Dict[str, dict] = field(default_factory=dict)
    mini_tool_history: List[dict] = field(default_factory=list)
    pairing_file_present: bool = False
    pairing_file_valid: bool = False
    pairing_status_message: Optional[str] = None

    def connect(self, device: Device, assume_trusted: bool = True):
        device.connected = True
        # If assume_trusted, mark trusted; otherwise keep prior trust flag
        device.trusted = device.trusted or assume_trusted
        self.device = device
        self.logs.append(f"device:{device.name}:connected")
        return device

    def reconnect(self):
        if not self.device:
            raise RuntimeError("No device to reconnect")
        self.device.connected = True
        self.logs.append(f"device:{self.device.name}:reconnected")
        return self.device

    def enable_jit(self, bundle_id: str):
        if not self.device or not self.device.connected:
            raise ValueError("A connected device is required for JIT enablement")
        self.jit_enabled_bundles.add(bundle_id)
        self.logs.append(f"jit:{bundle_id}:enabled")
        return True

    def start_log_stream(self, bundle_id: str):
        self.logs.append(f"log:{bundle_id}:stream-started")

    def emit_log(self, bundle_id: str, line: str):
        self.logs.insert(0, f"log:{bundle_id}:{line}")  # newest first

    def filter_logs(self, bundle_id: str) -> List[str]:
        return [line for line in self.logs if f"log:{bundle_id}:" in line]

    def add_mini_tool(self, name: str, behavior: str = "stable"):
        self.mini_tool_catalog[name] = {"behavior": behavior}

    def run_mini_tool(self, name: str, payload: str):
        meta = self.mini_tool_catalog.get(name, {"behavior": "stable"})
        if meta.get("behavior") == "crashy":
            result = {
                "name": name,
                "payload": payload,
                "status": "failed",
                "error": f"{name} reported a runtime error",
            }
        else:
            result = {
                "name": name,
                "payload": payload,
                "status": "succeeded",
                "output": f"{name} executed with payload {payload}",
            }
        self.mini_tool_history.append(result)
        self.logs.append(f"mini-tool:{name}:{result['status']}")
        return result

    def import_pairing_file(self, *, valid: bool):
        self.pairing_file_present = True
        self.pairing_file_valid = valid
        if valid:
            self.pairing_status_message = "Pairing file successfully imported"
        else:
            self.pairing_status_message = "Pairing file validation failed"
        return valid

    @property
    def can_start_connection(self) -> bool:
        return self.pairing_file_present and self.pairing_file_valid


@given('a tethered device named "{name}" running iOS {os_version}')
def step_tethered_device(context, name, os_version):
    context.device = Device(name=name, os_version=os_version)
    if not hasattr(context, "app"):
        context.app = StikDebugApp()


@given("I am connected to the device from StikDebug")
def step_connected(context):
    context.app.connect(context.device, assume_trusted=True)


@given("the device connection was previously trusted")
def step_previously_trusted(context):
    if not hasattr(context, "device"):
        context.device = Device(name="Unknown", os_version="unknown")
    context.device.trusted = True
    if not hasattr(context, "app"):
        context.app = StikDebugApp()
    context.app.device = context.device
    context.app.device.connected = True


@given('there is no connected device')
def step_no_device(context):
    context.app = StikDebugApp()
    context.device = None


@given("no pairing file has been imported")
def step_no_pairing_file(context):
    if not hasattr(context, "app"):
        context.app = StikDebugApp()
    context.app.pairing_file_present = False
    context.app.pairing_file_valid = False
    context.app.pairing_status_message = None


@given('the mini tool catalog contains "{tool_name}"')
def step_tool_catalog(context, tool_name):
    behavior = "crashy" if "Crashy" in tool_name else "stable"
    context.app.add_mini_tool(tool_name, behavior=behavior)


@when("I connect to the device from StikDebug")
def step_connect(context):
    context.app.connect(context.device)


@when("the USB session is restarted")
def step_reconnect(context):
    context.app.reconnect()


@when('I enable JIT for "{bundle_id}"')
def step_enable_jit(context, bundle_id):
    context.jit_result = context.app.enable_jit(bundle_id)
    context.last_bundle = bundle_id


@when('I try to enable JIT for "{bundle_id}"')
def step_try_enable_jit(context, bundle_id):
    try:
        context.app.enable_jit(bundle_id)
        context.error = None
    except Exception as exc:  # noqa: BLE001
        context.error = exc


@when('I run the mini tool "{tool_name}" with payload "{payload}"')
def step_run_mini_tool(context, tool_name, payload):
    context.mini_tool_result = context.app.run_mini_tool(tool_name, payload)


@when('I start live logging for bundle "{bundle_id}"')
def step_start_logging(context, bundle_id):
    context.last_bundle = bundle_id
    context.app.start_log_stream(bundle_id)


@when('the device emits a log line "{message}" for "{bundle_id}"')
def step_emit_log(context, message, bundle_id):
    context.app.emit_log(bundle_id, message)


@when("I import a valid pairing file")
def step_import_valid_pairing_file(context):
    context.import_result = context.app.import_pairing_file(valid=True)


@when("I import an invalid pairing file")
def step_import_invalid_pairing_file(context):
    context.import_result = context.app.import_pairing_file(valid=False)


@then('the device status should be "{expected}"')
def step_status(context, expected):
    status = "connected" if context.app.device and context.app.device.connected else "disconnected"
    assert status == expected, f"Expected {expected}, got {status}"


@then("the device trust handshake should be stored")
def step_trust(context):
    assert context.app.device and context.app.device.trusted, "Trust was not recorded"


@then('I should see the OS version "{os_version}"')
def step_os_version(context, os_version):
    assert context.app.device.os_version == os_version


@then("StikDebug should reconnect without a trust prompt")
def step_no_prompt(context):
    assert context.app.device and context.app.device.trusted, "Trust should persist across reconnect"


@then('the app should run with JIT privileges for "{bundle_id}"')
def step_jit_enabled(context, bundle_id):
    assert bundle_id in context.app.jit_enabled_bundles


@then('a console log should mention "{bundle_id}" JIT state')
def step_jit_log(context, bundle_id):
    matching = [line for line in context.app.logs if f"jit:{bundle_id}:enabled" in line]
    assert matching, "No JIT log recorded"


@then("I should be told the operation requires a connected device")
def step_jit_error(context):
    assert isinstance(context.error, ValueError)


@then("the mini tool run should be marked successful")
def step_tool_success(context):
    assert context.mini_tool_result["status"] == "succeeded"


@then('the run output should include "{fragment}"')
def step_tool_output(context, fragment):
    assert fragment in context.mini_tool_result.get("output", "")


@then("the run history should include the latest payload")
def step_history(context):
    assert context.mini_tool_result in context.app.mini_tool_history


@then("the run should fail with a helpful error message")
def step_tool_failure(context):
    assert context.mini_tool_result["status"] == "failed"
    assert "error" in context.mini_tool_result


@then("the app should report the pairing file import succeeded")
def step_pairing_success(context):
    assert context.import_result is True
    assert context.app.pairing_status_message == "Pairing file successfully imported"


@then("StikDebug should be ready to start device connection")
def step_pairing_ready(context):
    assert context.app.can_start_connection, "Expected connection flow to be unlocked"


@then("the app should report the pairing file is invalid")
def step_pairing_invalid(context):
    assert context.import_result is False
    assert context.app.pairing_status_message == "Pairing file validation failed"


@then("StikDebug should block device connection until a valid pairing file is imported")
def step_pairing_blocked(context):
    assert not context.app.can_start_connection, "Connection flow should remain blocked"


@then("the log stream should show the latest entry first")
def step_log_order(context):
    filtered = context.app.filter_logs(context.last_bundle)
    assert filtered and filtered[0].endswith("Render loop started"), "Latest log should be first"


@then('only logs for "{bundle_id}" should appear')
def step_log_filter(context, bundle_id):
    filtered = context.app.filter_logs(bundle_id)
    assert filtered and all(f"log:{bundle_id}:" in line for line in filtered)


@then("the log stream should retain earlier lines after reconnect")
def step_log_retain(context):
    filtered = context.app.filter_logs(context.last_bundle)
    assert any("loaded" in line for line in filtered), "Pre-reconnect log missing"
    assert any("Session restored" in line for line in filtered), "Post-reconnect log missing"
