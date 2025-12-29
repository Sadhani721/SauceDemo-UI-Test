from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def login_and_add_product(driver, count=1):
    LoginPage(driver).login("standard_user", "secret_sauce")
    products = ProductsPage(driver)
    products.add_products(count)
    products.go_to_cart()


# TC01 – Verify Cart page navigation

def test_cart_page_navigation(driver):
    login_and_add_product(driver)
    assert "cart" in driver.current_url


# TC02 – Verify Cart page title

def test_cart_page_title(driver):
    login_and_add_product(driver)
    cart = CartPage(driver)
    assert cart.get_title() == "Your Cart"


# TC03 – Verify added products displayed in Cart

def test_cart_items_displayed(driver):
    login_and_add_product(driver, 2)
    cart = CartPage(driver)
    assert cart.get_cart_items_count() == 2


# TC04 – Remove single product from Cart

def test_remove_single_item(driver):
    login_and_add_product(driver, 1)
    cart = CartPage(driver)
    cart.remove_first_item()
    assert cart.get_cart_items_count() == 0

# TC06 – Continue Shopping button

def test_continue_shopping(driver):
    login_and_add_product(driver, 1)
    cart = CartPage(driver)
    cart.click_continue_shopping()
    assert "inventory" in driver.current_url



# TC07 – Checkout navigation

def test_checkout_navigation(driver):
    login_and_add_product(driver, 1)
    cart = CartPage(driver)
    cart.click_checkout()
    assert "checkout" in driver.current_url