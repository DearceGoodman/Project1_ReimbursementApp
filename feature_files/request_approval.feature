Feature: Request Approval

  Scenario Outline: Request approval
    Given The manager is on the request approval page
    When The manager enters <ticket> into request ticket box
    When The manager enters <status> into request status box
    When The manager enters <comment> into manager comment box
    When The manager clicks the submit button
    When The manager clicks on the manager dashboard button
    Then The manager will be redirected to the <title>


  Examples:
    | ticket | status   | comment                | title |
    | 10     | approved | documentation approved | Manager Dashboard     |