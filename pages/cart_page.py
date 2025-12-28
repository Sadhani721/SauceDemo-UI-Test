from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BTNS = (By.CSS_SELECTOR, ".cart_item button")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def get_title(self):
        return self.wait_for_visible(self.CART_TITLE).text

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def remove_first_item(self):
        buttons = self.driver.find_elements(*self.REMOVE_BTNS)
        if buttons:
            buttons[0].click()

    def remove_all_items(self):
        buttons = self.driver.find_elements(*self.REMOVE_BTNS)
        for button in buttons:
            button.click()



