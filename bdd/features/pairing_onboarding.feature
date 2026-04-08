Feature: Pairing file onboarding
  To prepare a device for on-device debugging
  As a StikDebug user
  I want pairing file import to clearly enable or block the connection flow

  Background:
    Given a tethered device named "Test iPhone" running iOS 17.5
    And no pairing file has been imported

  Scenario: Import a valid pairing file
    When I import a valid pairing file
    Then the app should report the pairing file import succeeded
    And StikDebug should be ready to start device connection

  Scenario: Reject an invalid pairing file
    When I import an invalid pairing file
    Then the app should report the pairing file is invalid
    And StikDebug should block device connection until a valid pairing file is imported
