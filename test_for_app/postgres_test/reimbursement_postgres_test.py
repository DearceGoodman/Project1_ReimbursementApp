from data_access_layer.implementation.reimbursement_dao_imp import ReimbursementDAOImp
from data_access_layer.implementation.reimbursement_postgres_dao import ReimbursementPostgresDAO

from entities.reimbursement import Reimbursement

# add a postgres Employee and test
reimbursement_postgres_dao = ReimbursementPostgresDAO()
reimbursement_dao_imp = ReimbursementDAOImp()
reimbursement = Reimbursement("Test", "Player", 12, 103, "food", 0, "pending", "pending")
reimbursement_two = Reimbursement("Isassas", "Baker", 102, 103, "food", 0, "pending", "pending")
reimbursement_for_postgres = Reimbursement("Ezra", "Goodman", 326, 103, "food", 0, "pending", "pending")


def test_create_customer_success():
    new_reimbursement: Reimbursement = reimbursement_postgres_dao.create_reimbursement_entry(reimbursement_for_postgres)
    print(new_reimbursement.employee_id)
    assert new_reimbursement.employee_id != 0


def test_view_employee_request():
    reimbursements = reimbursement_postgres_dao.view_employee_requests(323)
    assert len(reimbursements) == 6


def test_get_all_request_tickets():
    result = reimbursement_postgres_dao.get_all_request_tickets()
    return result


# failed need to fix
def test_update_status_judgement():
    updated_reimbursement = reimbursement_postgres_dao.update_status_judgement(reimbursement_for_postgres)
    assert updated_reimbursement.request_status == "pending"
