from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class EmployeeDashboardPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "logoutButton")
        return element

    def create_request_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createReimbursement")
        return element
