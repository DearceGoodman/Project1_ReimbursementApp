from statistics import mean
from typing import List

from custom_exception.duplicate_employee_id_exception import DuplicateEmployeeIdException
from data_access_layer.implementation.reimbursement_postgres_dao import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service.abstract.reimbursement_dao_service import ReimbursementService


class ReimbursementPostgresService(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementPostgresDAO):
        self.reimbursement_dao = reimbursement_dao

    # need to check and make sure employee do not have the same employee id
    def service_create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursements = self.reimbursement_dao.get_all_request_tickets()
        for existing_reimbursement in reimbursements:
            if existing_reimbursement.request_ticket == reimbursement.request_ticket:
                raise DuplicateEmployeeIdException("Ticket is already taken!")
        created_reimbursement = self.reimbursement_dao.create_reimbursement_entry(reimbursement)
        return created_reimbursement

    def service_view_employee_requests(self, employee_id: int) -> List[Reimbursement]:
        result = self.reimbursement_dao.view_employee_requests(employee_id)
        return result

    def service_get_all_request_tickets(self) -> list[Reimbursement]:
        return self.reimbursement_dao.get_all_request_tickets()

    def service_update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursements = self.reimbursement_dao.get_all_request_tickets()
        for current_reimbursement in reimbursements:
            if current_reimbursement.employee_id != reimbursement.employee_id:
                updated_reimbursement = self.reimbursement_dao.update_status_judgement(reimbursement)
                return updated_reimbursement

    def service_statistics_average_reimbursement(self, employee_id: int):
        requests = self.reimbursement_dao.view_employee_requests(employee_id)
        reimburse = []
        for request in requests:
            if request.request_amount == 1:
                reimburse.append(request.request_amount)
        return mean(reimburse)
