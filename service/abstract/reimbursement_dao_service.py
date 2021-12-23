from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):
    # create player method
    @abstractmethod
    def service_create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # get request ticket
    @abstractmethod
    def service_view_employee_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    # get all requests
    @abstractmethod
    def service_get_all_request_tickets(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_statistics_average_reimbursement(self, employee_id: int):
        pass
