Feature: Emp Login

  Scenario Outline: as a employee i want to login into site
    Given The employee is on login page
    When The employee enters <username> into username input box
    When The employee enters <password> into password input box
    When The employee clicks the login button
    Then The employee should be redirected to the <title> dashboard page

    Examples: Emp login
      | username | password | title              |
      | username | password | Employee Dashboard |

