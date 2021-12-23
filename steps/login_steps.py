import time

from behave import Given, When, Then


@Given(u'The employee is on login page')
def get_employee_login_page(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/login.html")


# problem here
@When(u'The employee enters {username} into username input box')
def enter_username(context, username: str):
    context.login_page.select_input_username().send_keys(username)


@When(u'The employee enters {password} into password input box')
def enter_password(context, password: str):
    context.login_page.select_input_password().send_keys(password)


@When(u'The employee clicks the login button')
def click_login(context):
    context.login_page.select_login_button().click()


@Then(u'The employee should be redirected to the {title} dashboard page')
def check_employee_dashboard(context, title: str):
    time.sleep(2)
    assert context.driver.title == title
