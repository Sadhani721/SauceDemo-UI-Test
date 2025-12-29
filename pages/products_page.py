from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class ProductsPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, ".inventory_item button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRICES = (By.CLASS_NAME, "inventory_item_price")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    def sort_low_to_high(self):
        Select(self.wait_for_visible(self.SORT_DROPDOWN)).select_by_value("lohi")

    def add_items_to_cart(self, count=2):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        for i in range(count):
            buttons[i].click()

    def add_products(self, count=1):
        """Alias for add_items_to_cart"""
        self.add_items_to_cart(count)

    def get_cart_count(self):
        return self.wait_for_visible(self.CART_BADGE).text

    def get_cart_badge_count(self):
        """Alias for get_cart_count"""
        return self.get_cart_count()

    def go_to_cart(self):
        # Navigate directly to cart page (more reliable than clicking)
        self.driver.get("https://www.saucedemo.com/cart.html")

        # Wait for cart page to load
        self.wait.until(EC.url_contains("cart"))

    def get_prices(self):
        return [float(p.text.replace("$", "")) for p in self.driver.find_elements(*self.PRICES)]

    def logout(self):
        self.click(self.MENU_BTN)
        # Wait for menu to slide out and logout button to be visible
        time.sleep(0.5)
        self.click(self.LOGOUT_BTN)