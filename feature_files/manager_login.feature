Feature: Manager Login

  Scenario Outline: as a manager i want to login into site
    Given The manager is on login page
    When The manager enters <username> into username input box
    When The manager enters <password> into password input box
    When The manager clicks the login button
    Then The manager should be redirected to the manager dashboard page

    Examples: Manager login
      | username | password |
      | username | password |
