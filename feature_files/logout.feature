Feature: Employee Logout

  Scenario Outline: Employee logout
    Given Employee is on the Employee Dashboard Page
    When Employee clicks the logout button
    Then The employee is redirected to the <title>

  Examples:
    | title    |
    | HomePage |
