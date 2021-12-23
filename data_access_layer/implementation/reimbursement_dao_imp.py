from typing import List

from data_access_layer.abstract.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement


class ReimbursementDAOImp(ReimbursementDAO):
    # these requests are pre_made so that we can test our methods
    pre_made_request = Reimbursement("John", "Doe", 100, 250, "extended stay", 1, "pending", "pending")
    pre_made_request_two = Reimbursement("Jane", "Doe", 101, 300, "gas", 2, "pending", "pending")
    pre_made_delete = Reimbursement("Delete", "Doe", 102, 50, "food expense", 3, "pending", "pending")

    # we are going to use this list as our "database"
    requests_list = [pre_made_request, pre_made_request_two, pre_made_delete]
    # we are going to use this value to assign unique player ids
    employee_request_generator = 4

    def create_reimbursement_entry(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursement.request_ticket_number = ReimbursementDAOImp.employee_request_generator
        ReimbursementDAOImp.employee_request_generator += 1
        ReimbursementDAOImp.requests_list.append(reimbursement)
        return reimbursement

    def view_employee_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    def get_all_request_tickets(self) -> list[Reimbursement]:
        pass

    def update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
