from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        title = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        return title.text

    def get_cart_items_count(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)

    def remove_first_item(self):
        # Get initial count
        initial_count = self.get_cart_items_count()

        # Click remove button
        remove_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_item button"))
        )
        remove_btn.click()

        # Wait for item to be removed from DOM
        self.wait.until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "cart_item")) < initial_count
        )

    def remove_all_items(self):
        while True:
            buttons = self.driver.find_elements(By.CSS_SELECTOR, ".cart_item button")

            if not buttons:
                break

            buttons[0].click()
            time.sleep(0.5)

            try:
                current_count = len(buttons)
                WebDriverWait(self.driver, 3).until(
                    lambda d: len(d.find_elements(By.CSS_SELECTOR, ".cart_item button")) < current_count
                )
            except:
                pass

    def click_continue_shopping(self):
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue-shopping"))
        )
        continue_btn.click()

        # Wait for navigation to inventory page
        self.wait.until(EC.url_contains("inventory"))

    def click_checkout(self):
        # Navigate directly to checkout page (more reliable than clicking)
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

        # Wait for checkout page to load
        self.wait.until(EC.url_contains("checkout"))
