from custom_exception.duplicate_employee_id_exception import DuplicateEmployeeIdException
from data_access_layer.implementation.reimbursement_dao_imp import ReimbursementDAOImp
from entities.reimbursement import Reimbursement
from service.abstract.reimbursement_dao_service import ReimbursementService


class ReimbursementServiceImp(ReimbursementService):

    def __init__(self, reimbursement_dao):
        self.reimbursement_dao: ReimbursementDAOImp = reimbursement_dao

    def service_create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        for current_reimbursement in self.reimbursement_dao.requests_list:
            if current_reimbursement.request_ticket == reimbursement.request_ticket:
                if current_reimbursement.request_amount <= 0:
                    raise DuplicateEmployeeIdException("Enter Valid Request!")
            else:
                return self.reimbursement_dao.create_reimbursement_entry(reimbursement)

    def service_view_employee_requests(self, employee_id: int) -> Reimbursement:
        pass

    def service_get_all_request_tickets(self) -> list[Reimbursement]:
        pass

    def service_update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_statistics_average_reimbursement(self):
        pass
