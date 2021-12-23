from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RequestApprovalPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_ticket(self):
        element: WebElement = self.driver.find_element(By.ID, "requestTicket")
        return element

    def select_request_status(self):
        element: WebElement = self.driver.find_element(By.ID, "requestStatus")
        return element

    def select_manager_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "managerComment")
        return element

    def select_submit_decision(self):
        element: WebElement = self.driver.find_element(By.ID, "approvalDenyButton")
        return element

    def select_manager_dashboard(self):
        element: WebElement = self.driver.find_element(By.ID, "transferToMgrDashboard")
        return element
