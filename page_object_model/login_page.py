from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_input_username(self):
        # this will return web element by given id
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def select_input_password(self):
        # this will return web element by given id
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def select_login_button(self):
        # this will return web element by given id
        element: WebElement = self.driver.find_element(By.ID, "loginButton")
        return element
