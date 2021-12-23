
from behave import Given, When, Then

@Given(u'The manager is on the request approval page')
def check_approval_page(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/reimbursementApproval.html")


@When(u'The manager enters {ticket} into request ticket box')
def enter_ticket(context, ticket: int):
    context.request_approval_page.select_ticket().send_keys(ticket)


@When(u'The manager enters {status} into request status box')
def enter_status(context, status: str):
    context.request_approval_page.select_request_status().send_keys(status)


@When(u'The manager enters {comment} into manager comment box')
def enter_comment(context, comment: str):
    context.request_approval_page.select_manager_comment().send_keys(comment)


@When(u'The manager clicks the submit button')
def click_manager_submit(context):
    context.request_approval_page.select_submit_decision().click()


@When(u'The manager clicks on the manager dashboard button')
def click_manager_dashboard_button(context):
    context.request_approval_page.select_manager_dashboard().click()


@Then(u'The manager will move to the <title>')
def check_manager_dashboard_page(context, title: str):
    assert context.driver.title == title
