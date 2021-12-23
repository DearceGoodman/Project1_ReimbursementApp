from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class SubmitReimbursementPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_firstname_input(self):
        element: WebElement = self.driver.find_element(By.ID, "firstName")
        return element

    def select_lastname_input(self):
        element: WebElement = self.driver.find_element(By.ID, "lastName")
        return element

    def select_employee_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeId")
        return element

    def select_request_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "requestAmount")
        return element

    def select_employee_comment_input(self):
        element: WebElement = self.driver.find_element(By.ID, "employeeComment")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "submitReimbursement")
        return element

    def select_employee_dashboard_button(self):
        element: WebElement = self.driver.find_element(By.ID, "transferToEmpDashboard")
        return element
