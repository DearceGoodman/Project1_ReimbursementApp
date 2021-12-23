from data_access_layer.implementation.login_dao_postgres import LoginPostgresDAO

login_dao = LoginPostgresDAO()
username = "username"
password = "password"


def test_validate_login():
    validated = login_dao.get_login_by_credentials(username, password)
    assert validated


def test_not_validate_login():
    validated = login_dao.get_login_by_credentials("bad username", "bad password")
    if validated:
        assert False
    else:
        assert True
