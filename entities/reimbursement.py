class Reimbursement:
    def __init__(self, first_name: str, last_name: str, employee_id: int, request_amount: int, employee_comment: str,
                 request_ticket: int, request_status: str, manager_comment: str):

        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.request_amount = request_amount
        self.employee_comment = employee_comment
        self.request_ticket = request_ticket
        self.request_status = request_status
        self.manager_comment = manager_comment

    def make_reimbursement_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "employeeId": self.employee_id,
            "requestAmount": self.request_amount,
            "employeeComment": self.employee_comment,
            "requestTicket": self.request_ticket,
            "requestStatus": self.request_status,
            "managerComment": self.manager_comment
        }

    def __str__(self):
        return "first name: {}, last name: {}, employee id: {}, request_amount: {}, request_ticket_number: {}, " \
               "request_status: {}".format(self.first_name, self.last_name, self.employee_id, self.request_amount,
                                           self.employee_comment, self.request_ticket, self.request_status,
                                           self.manager_comment)
