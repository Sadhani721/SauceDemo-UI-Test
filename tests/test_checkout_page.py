from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def navigate_to_checkout(driver):

    LoginPage(driver).login("standard_user", "secret_sauce")
    products = ProductsPage(driver)
    products.add_products(1)
    products.go_to_cart()
    CartPage(driver).click_checkout()


# TC01 – Navigate to Checkout page (Step One)

def test_checkout_navigation(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    assert checkout.is_on_step_one()


# TC03 – Valid checkout information → Step Two

def test_checkout_valid_information(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("Test", "User", "12345")

    # Stable validation (URL + element wait)
    assert checkout.is_on_step_two()


# TC04 – Empty First Name

def test_checkout_empty_first_name(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # 🔥 Use None instead of empty string
    checkout.fill_checkout_info(None, "User", "12345")

    assert "Error" in checkout.get_error_message()


# TC05 – Empty Last Name

def test_checkout_empty_last_name(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("Test", None, "12345")

    assert "Error" in checkout.get_error_message()


# TC06 – Empty Postal Code

def test_checkout_empty_postal_code(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("Test", "User", None)

    assert "Error" in checkout.get_error_message()


# TC08 – Cancel checkout from Step One

def test_cancel_checkout_from_info_page(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    assert checkout.is_on_step_one()

    checkout.click_cancel()

    # Cancel navigation is async → wait handled in page
    assert "cart" in driver.current_url


# TC12 – Complete checkout successfully

def test_complete_checkout(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("Test", "User", "12345")
    assert checkout.is_on_step_two()

    checkout.click_finish()

    assert checkout.get_success_message() == "THANK YOU FOR YOUR ORDER"


# TC16 – Back Home after order completion

def test_back_home_after_checkout(driver):
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    checkout.fill_checkout_info("Test", "User", "12345")
    assert checkout.is_on_step_two()

    checkout.click_finish()
    checkout.click_back_home()

    assert "inventory" in driver.current_url