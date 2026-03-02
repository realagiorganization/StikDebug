Feature: Device connection lifecycle
  In order to debug and enable JIT on connected devices
  As a StikDebug maintainer
  I want to prove the app models trusted connections and reconnections safely

  Background:
    Given a tethered device named "Test iPhone" running iOS 17.5

  Scenario: Connect to a trusted device once
    When I connect to the device from StikDebug
    Then the device status should be "connected"
    And the device trust handshake should be stored
    And I should see the OS version "17.5"

  Scenario: Reconnect after a dropped link without prompting trust
    Given the device connection was previously trusted
    When the USB session is restarted
    Then StikDebug should reconnect without a trust prompt
    And the device status should be "connected"
