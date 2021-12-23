from data_access_layer.abstract.manager_login_dao import ManagerLoginDAO
from util.database_connection import connection


class ManagerLoginPostgresDAO(ManagerLoginDAO):

    def get_manager_login_by_credentials(self, username: str, password: str):
        sql = "select login_id from login where username= %s and password= %s"
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))
        validated = cursor.fetchone()
        return validated
