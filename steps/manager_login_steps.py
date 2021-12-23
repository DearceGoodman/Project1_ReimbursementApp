import time

from behave import Given, When, Then


@Given(u'The manager is on login page')
def get_manager_login_page(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/manager_login.html")


# problem here
@When(u'The manager enters {username} into username input box')
def enter_username(context, username: str):
    context.manager_login_page.select_input_username().send_keys(username)


@When(u'The manager enters {password} into password input box')
def enter_password(context, password: str):
    context.manager_login_page.select_input_password().send_keys(password)


@When(u'The manager clicks the login button')
def click_login(context):

    context.manager_login_page.select_login_button().click()


@Then(u'The manager should be redirected to the manager dashboard page')
def check_manager_dashboard(context):

    title = context.driver.title
    assert title == "Manager Dashboard"
