from typing import List

from data_access_layer.abstract.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementPostgresDAO(ReimbursementDAO):
    def create_reimbursement_entry(self, reimbursement: Reimbursement) -> Reimbursement:
        # we will use %s as placeholders for our values
        sql = "insert into reimbursement values(%s, %s, %s, %s, %s, default, %s, %s) returning request_ticket"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.first_name, reimbursement.last_name, reimbursement.employee_id,
                             reimbursement.request_amount, reimbursement.employee_comment, reimbursement.request_status,
                             reimbursement.manager_comment))
        connection.commit()
        request_ticket = cursor.fetchone()[0]
        reimbursement.request_ticket = request_ticket
        return reimbursement

    def view_employee_requests(self, employee_id: int) -> List[Reimbursement]:
        sql = "select * from reimbursement where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimbursement_records = cursor.fetchall()
        reimbursements = []
        for reimbursement in reimbursement_records:
            reimbursements.append(Reimbursement(*reimbursement))
        return reimbursements

    def get_all_request_tickets(self) -> list[Reimbursement]:
        sql = "select * from reimbursement"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def update_status_judgement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update reimbursement set request_status = %s, manager_comment = %s where request_ticket = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.request_status, reimbursement.manager_comment, reimbursement.request_ticket))
        connection.commit()
        return reimbursement
