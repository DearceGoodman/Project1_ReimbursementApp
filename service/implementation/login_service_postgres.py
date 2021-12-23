from data_access_layer.implementation.login_dao_postgres import LoginPostgresDAO
from service.abstract.login_service import LoginService


class LoginPostgresService(LoginService):
    def __init__(self, login_dao: LoginPostgresDAO):
        self.login_dao = login_dao

    def validate_login(self, username, password):
        validation = self.login_dao.get_login_by_credentials(username, password)
        if type(validation) == tuple:
            return True
        else:
            return False
