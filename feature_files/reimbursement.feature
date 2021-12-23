Feature: Emp Reimbursement

    Scenario Outline: Employee creates and submits a reimbursement
        Given The employee is on the Employee Dashboard Page
        When The employee clicks on the Create Reimbursement Request
        When The employee will be redirected to the Submit Reimbursement Page
        When The employee enters <value> into the first name box
        When The employee enters <lastname> into the last name box
        When The employee enters <employeeid> into the employee id box
        When The employee enters <requestamount> into the request amount box
        When The employee enters <employeecomment> into the employee comment box
        When The employee clicks the submit button
        When The employee clicks the employee dashboard button
        Then The employee gets redirected to the <title> page


    Examples:Emp reimbursement
        | value  | lastname | employeeid | requestamount | employeecomment | title              |
        | Dearce | Goodman  | 111        | 250           | Hotel Stay      | Employee Dashboard |