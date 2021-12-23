from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    # create reimbursement method
    @abstractmethod
    def create_reimbursement_entry(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # get request ticket
    @abstractmethod
    def view_employee_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    # get all requests
    @abstractmethod
    def get_all_request_tickets(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
