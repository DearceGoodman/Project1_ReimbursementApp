from behave.runner import Context
from selenium import webdriver

from page_object_model.employee_dashboard_page import EmployeeDashboardPage
from page_object_model.login_page import LoginPage
from page_object_model.manager_dashboard_page import ManagerDashboardPage
from page_object_model.manager_login_page import ManagerLoginPage
from page_object_model.request_approval_page import RequestApprovalPage
from page_object_model.submit_reimbursement_page import SubmitReimbursementPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.login_page = LoginPage(context.driver)
    context.submit_reimbursement_page = SubmitReimbursementPage(context.driver)
    context.employee_dashboard_page = EmployeeDashboardPage(context.driver)
    context.manager_login_page = ManagerLoginPage(context.driver)
    context.manager_dashboard_page = ManagerDashboardPage(context.driver)
    context.request_approval_page = RequestApprovalPage(context.driver)


def after_all(context):
    context.driver.quit()
