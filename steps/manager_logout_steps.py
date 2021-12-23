from behave import Given, When, Then


@Given(u'The manager is in the manager dashboard page')
def check_manager_dashboard_page(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/manager_dashboard.html")


@When(u'The manager clicks the logout button')
def click_logout_button(context):
    context.manager_dashboard_page.manager_logout_button().click()


@Then(u'The manager will be redirected to the {title}')
def check_home_page(context, title: str):
    assert context.driver.title == title
