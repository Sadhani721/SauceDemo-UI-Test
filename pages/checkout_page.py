from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    CANCEL_BTN = (By.ID, "cancel")
    BACK_HOME_BTN = (By.ID, "back-to-products")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_checkout_info(self, first_name="John", last_name="Doe", postal_code="12345"):
        """Fill checkout form with provided information and click continue"""
        # Only fill fields that are not None (None means leave empty for validation testing)
        if first_name is not None:
            self.type(self.FIRST_NAME, first_name)
        if last_name is not None:
            self.type(self.LAST_NAME, last_name)
        if postal_code is not None:
            self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def click_finish(self):
        """Alias for finish_checkout"""
        self.click(self.FINISH_BTN)

    def click_cancel(self):
        """Click the cancel button"""
        self.click(self.CANCEL_BTN)

    def click_back_home(self):
        """Click the back home button after order completion"""
        self.click(self.BACK_HOME_BTN)

    def get_success_message(self):
        return self.wait_for_visible(self.SUCCESS_MSG).text

    def get_error_message(self):
        """Get the error message text"""
        return self.wait_for_visible(self.ERROR_MSG).text

    def is_on_step_one(self):
        """Check if we are on checkout step one (information page)"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.FIRST_NAME)
            )
            return "checkout-step-one" in self.driver.current_url
        except:
            return False

    def is_on_step_two(self):
        """Check if we are on checkout step two (overview page)"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.FINISH_BTN)
            )
            return "checkout-step-two" in self.driver.current_url
        except:
            return False

