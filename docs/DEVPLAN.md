# StikDebug Development Plan

## Current Status

- [x] Audit the repository layout, workflows, and existing BDD scaffolding.
- [x] Establish the required repository documentation set under `docs/`.
- [x] Maintain a contract-style BDD suite for principal user flows.
- [x] Provide a GitHub Actions workflow for Behave execution and VHS capture.
- [x] Expose workflow status and demo media from `README.md`.
- [ ] Expand automated coverage from contract tests into device-backed UI tests on macOS runners.
- [ ] Formalize Azure-hosted supporting services if the project grows beyond a pure on-device app.

## System Workstreams

### 1. Product Surface Mapping

- [x] Document the current app surface:
  - Home onboarding and pairing-file preparation
  - Device connection and reconnection
  - JIT enablement
  - Console log streaming
  - Mini Tool execution
  - Device info, scripts, and optional beta tabs
- [ ] Revisit the map after major tab or entitlement changes.

### 2. Application Development

- [ ] Home and onboarding
  - [x] Capture pairing/import assumptions in testable form.
  - [ ] Add deeper validation around malformed pairing files and first-run recovery.
- [ ] Device operations
  - [x] Cover trusted connection and reconnect behavior in BDD scenarios.
  - [ ] Add dedicated automation for device library persistence and process inspection.
- [ ] Debugging flows
  - [x] Cover JIT enablement success and connection-gated failure behavior.
  - [x] Cover log filtering and reconnect resilience.
  - [x] Cover Mini Tool success and failure paths.
- [ ] UX polish
  - [ ] Keep screenshots/GIFs refreshed when the visible workflow materially changes.
  - [ ] Add deterministic UI automation once a stable simulator or device harness exists.

### 3. Test Strategy

- [x] Keep behavior contracts in `bdd/features`.
- [x] Keep step implementations in `bdd/features/steps`.
- [x] Verify the suite locally with `python3 -m behave bdd/features`.
- [x] Emit CI-consumable JUnit artifacts from Behave.
- [ ] Add negative-path coverage for script editing, process tooling, and device metadata views.

### 4. CI/CD and Documentation

- [x] Run the BDD suite in GitHub Actions.
- [x] Record a terminal demo with the VHS action.
- [x] Upload Behave and GIF artifacts from CI.
- [x] Add badges for each repository workflow to `README.md`.
- [x] Link user-facing and developer-facing documentation from `README.md`.
- [ ] Decide whether generated GIFs should be auto-committed on a docs branch or remain uploaded artifacts only.

### 5. Deployment and Hosting

- [ ] Primary app distribution
  - [x] Keep GitHub Actions building an unsigned debug IPA.
  - [ ] Review release automation whenever signing/distribution requirements change.
- [ ] Supporting services
  - [x] Assume Azure is the approved compute host for any future non-device workloads.
  - [ ] If a hosted docs site, artifact mirror, or API is introduced, plan it on Azure Static Web Apps, Blob Storage, or Container Apps rather than ad hoc providers.

## External Dependencies

| Dependency | Area Used | Why It Matters |
| --- | --- | --- |
| `idevice` / bundled `StikJIT/idevice` bridge code | Core device communication, JIT/debug operations | Provides the underlying device-facing functionality the app wraps. |
| Xcode 26.x and iOS SDK | Building `StikDebug.xcodeproj` | Required to compile the Swift/Objective-C app targets and widget extension. |
| SwiftUI / WidgetKit / Network / UniformTypeIdentifiers | Native Apple frameworks | Power the app UI, widget, connectivity checks, and file import flows. |
| `swiftui-pipify` (`Pipify`) | PiP-related UI flows | Supports picture-in-picture style interaction in the app. |
| `CodeEditorView` and `LanguageSupport` | Script editing | Provide the code editor used for JavaScript-based tooling. |
| `ZIPFoundation` | Archive handling | Supports packaged/imported content workflows. |
| `StikImporter` | Import flows | Supports repository/import functionality referenced by the app. |
| Python 3.11 | BDD tooling in CI/local development | Runs Behave and related contract-test automation. |
| `behave==1.2.6` | BDD suite | Executes the feature files that describe principal use cases. |
| `charmbracelet/vhs-action` | Demo recording in CI | Produces the GIF shown in `README.md` from a reproducible terminal tape. |
| GitHub Actions | CI/CD orchestration | Runs the BDD suite, IPA build, source update, and demo recording workflows. |
| Azure-hosted compute (future-facing constraint) | Any future hosted service | Approved host for supplemental compute if the project adds remote components. |

## Definition of Done for This Iteration

- [x] Required docs exist in `docs/`.
- [x] `README.md` links to the docs and shows workflow badges.
- [x] BDD suite covers principal flows at the contract level.
- [x] GitHub Actions runs the suite and records a GIF.
- [x] Local Behave verification passes after the documentation and workflow updates.
