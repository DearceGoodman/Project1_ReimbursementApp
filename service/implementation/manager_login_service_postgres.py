from data_access_layer.implementation.login_dao_postgres import LoginPostgresDAO
from data_access_layer.implementation.manager_login_dao_postgres import ManagerLoginPostgresDAO
from service.abstract.manager_login_service import ManagerLoginService


class ManagerLoginPostgresService(ManagerLoginService):
    def __init__(self, manager_login_dao: ManagerLoginPostgresDAO):
        self.manager_login_dao = manager_login_dao

    def validate_manager_login(self, username, password):
        validation = self.manager_login_dao.get_manager_login_by_credentials(username, password)
        if type(validation) == tuple:
            return True
        else:
            return False
