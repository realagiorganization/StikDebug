Feature: JIT enablement
  So I can run performance-critical apps safely
  As a developer using StikDebug
  I want JIT enablement to be guarded by device connection state and auditable logs

  Background:
    Given a tethered device named "Test iPhone" running iOS 17.5
    And I am connected to the device from StikDebug

  Scenario Outline: Enable JIT for a sideloaded bundle
    When I enable JIT for "<bundle_id>"
    Then the app should run with JIT privileges for "<bundle_id>"
    And a console log should mention "<bundle_id>" JIT state

    Examples:
      | bundle_id                 |
      | com.example.delta        |
      | org.emulator.ppsspp      |
      | com.arcade.classics      |

  Scenario: Gracefully block JIT when no device is attached
    Given there is no connected device
    When I try to enable JIT for "com.example.missing"
    Then I should be told the operation requires a connected device
