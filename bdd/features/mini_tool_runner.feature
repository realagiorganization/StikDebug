Feature: Mini tool runner
  To automate device-side checks without rebuilding the app
  As a power user
  I want mini tools to report success, surface output, and retain history

  Background:
    Given a tethered device named "Test iPhone" running iOS 17.5
    And I am connected to the device from StikDebug
    And the mini tool catalog contains "Location Spoofer"

  Scenario: Run a mini tool with structured payload
    When I run the mini tool "Location Spoofer" with payload "{"latitude":38.8895,"longitude":-77.0353}"
    Then the mini tool run should be marked successful
    And the run output should include "Location Spoofer"
    And the run history should include the latest payload

  Scenario: Report a failing mini tool
    Given the mini tool catalog contains "Crashy Script"
    When I run the mini tool "Crashy Script" with payload "{}"
    Then the run should fail with a helpful error message
