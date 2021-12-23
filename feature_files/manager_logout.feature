Feature: Manager Logout

  Scenario Outline: Manager logout
    Given The manager is in the manager dashboard page
    When The manager clicks the logout button
    Then The manager will be redirected to the <title>

  Examples:
    | title    |
    | HomePage |