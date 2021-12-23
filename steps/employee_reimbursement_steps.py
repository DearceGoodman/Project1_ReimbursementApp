from behave import given, when, then
import time


@given(u'The employee is on the Employee Dashboard Page')
def check_employee_dashboard(context):
    context.driver.get("C:/Users/Isassas/PycharmProjects/project_one/templates/employee_dashboard.html")


@when(u'The employee clicks on the Create Reimbursement Request')
def click_reimbursement_button(context):
    context.employee_dashboard_page.create_request_button().click()


@when(u'The employee will be redirected to the Submit Reimbursement Page')
def check_submit_reimbursement_page(context):
    title = context.driver.title
    assert title == "Submit Reimbursement Page"
    time.sleep(1)


@when(u'The employee enters {value} into the first name box')
def enter_first_name(context, value: str):
    context.submit_reimbursement_page.select_firstname_input().send_keys(value)
    time.sleep(1)


@when(u'The employee enters {lastname} into the last name box')
def enter_last_name(context, lastname: str):
    context.submit_reimbursement_page.select_lastname_input().send_keys(lastname)


@when(u'The employee enters {employeeid} into the employee id box')
def employee_id_input(context, employeeid: int):
    context.submit_reimbursement_page.select_employee_id_input().send_keys(employeeid)


@when(u'The employee enters {requestamount} into the request amount box')
def request_amount_input(context, requestamount: int):
    context.submit_reimbursement_page.select_request_amount_input().send_keys(requestamount)


@when(u'The employee enters {employeecomment} into the employee comment box')
def employee_comment_input(context, employeecomment: str):
    context.submit_reimbursement_page.select_employee_comment_input().send_keys(employeecomment)


@when(u'The employee clicks the submit button')
def click_submit_button(context):
    context.submit_reimbursement_page.select_submit_button().click()
    time.sleep(1)


@when(u'The employee clicks the employee dashboard button')
def click_employee_dashboard_button(context):
    context.submit_reimbursement_page.select_employee_dashboard_button().click()


@then(u'The employee gets redirected to the {title} page')
def check_employee_dashboard(context, title: str):
    assert context.driver.title == title
