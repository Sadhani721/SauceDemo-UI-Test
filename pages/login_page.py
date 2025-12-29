from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def is_error_displayed(self):
        return self.wait_for_visible(self.ERROR_MSG).is_displayed()

    def get_error_message(self):
        return self.wait_for_visible(self.ERROR_MSG).text