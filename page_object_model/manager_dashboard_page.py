from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerDashboardPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manager_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutButton")
        return element

    def request_approval_button(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementApproval")
