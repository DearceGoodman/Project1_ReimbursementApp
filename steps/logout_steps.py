from behave import Given, When, Then


@Given(u'Employee is on the Employee Dashboard Page')
def get_employee_dashboard_page(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/employee_dashboard.html")


@When(u'Employee clicks the logout button')
def click_employee_logout(context):
    context.employee_dashboard_page.logout_button().click()


@Then(u'The employee is redirected to the {title}')
def check_homepage(context, title: str):
    assert context.driver.title == title
