from data_access_layer.implementation.manager_login_dao_postgres import ManagerLoginPostgresDAO
from service.implementation.manager_login_service_postgres import ManagerLoginPostgresService

manager_login_dao = ManagerLoginPostgresDAO()
manager_login_service = ManagerLoginPostgresService(manager_login_dao)
username = "username"
password = "password"


def test_validate_correct_credentials():
    validation = manager_login_service.validate_manager_login(username, password)
    assert validation


def test_catch_bad_username():
    validation = manager_login_service.validate_manager_login("bad username", password)
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_password():
    validation = manager_login_service.validate_manager_login(username, "bad password")
    if validation:
        assert False
    else:
        assert True


def test_catch_bad_username_and_password():
    validation = manager_login_service.validate_manager_login("bad username", "bad password")
    if validation:
        assert False
    else:
        assert True
