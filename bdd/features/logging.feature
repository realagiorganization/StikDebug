Feature: Live console logging
  In order to troubleshoot JIT and Mini Tools quickly
  As a developer
  I want filtered live logs that survive reconnects and highlight the latest entries

  Background:
    Given a tethered device named "Test iPhone" running iOS 17.5
    And I am connected to the device from StikDebug

  Scenario: Filter logs by bundle identifier
    When I start live logging for bundle "com.example.delta"
    And the device emits a log line "JIT enabled" for "com.example.delta"
    And the device emits a log line "Render loop started" for "com.example.delta"
    Then the log stream should show the latest entry first
    And only logs for "com.example.delta" should appear

  Scenario: Preserve tail across reconnect
    When I start live logging for bundle "org.emulator.ppsspp"
    And the device emits a log line "PPSSPP loaded" for "org.emulator.ppsspp"
    And the USB session is restarted
    And the device emits a log line "Session restored" for "org.emulator.ppsspp"
    Then the log stream should retain earlier lines after reconnect
