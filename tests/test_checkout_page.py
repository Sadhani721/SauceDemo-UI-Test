from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def navigate_to_checkout(driver):
    """Helper function: Login → Add products → Go to cart → Click checkout"""
    # Step 1: Login with correct credentials
    LoginPage(driver).login("standard_user", "secret_sauce")

    # Step 2: Add 2 products to cart
    products = ProductsPage(driver)
    products.add_products(2)

    # Step 3: Go to cart
    products.go_to_cart()

    # Step 4: Click checkout button
    CartPage(driver).click_checkout()


# TC01 – Navigate to Checkout page (Step One)
def test_checkout_navigation(driver):
    """Test: Verify user reaches checkout step one"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)
    assert checkout.is_on_step_one()
    assert "checkout-step-one" in driver.current_url


# TC02 – Valid checkout information → Step Two
def test_checkout_valid_information(driver):
    """Test: Fill checkout info and proceed to step two"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Fill checkout information
    checkout.fill_checkout_info("Test", "User", "12345")

    # Verify step two is reached
    assert checkout.is_on_step_two()
    assert "checkout-step-two" in driver.current_url


# TC03 – Empty First Name
def test_checkout_empty_first_name(driver):
    """Test: Error when first name is empty"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Try to continue without first name
    checkout.fill_checkout_info(None, "User", "12345")

    # Verify error message appears
    error = checkout.get_error_message()
    assert "First Name is required" in error or "Error" in error


# TC04 – Empty Last Name
def test_checkout_empty_last_name(driver):
    """Test: Error when last name is empty"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Try to continue without last name
    checkout.fill_checkout_info("Test", None, "12345")

    # Verify error message appears
    error = checkout.get_error_message()
    assert "Last Name is required" in error or "Error" in error


# TC05 – Empty Postal Code
def test_checkout_empty_postal_code(driver):
    """Test: Error when postal code is empty"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Try to continue without postal code
    checkout.fill_checkout_info("Test", "User", None)

    # Verify error message appears
    error = checkout.get_error_message()
    assert "Postal Code is required" in error or "Error" in error


# TC06 – Cancel checkout from Step One
def test_cancel_checkout_from_info_page(driver):
    """Test: Cancel button returns to cart"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Verify we're on step one
    assert checkout.is_on_step_one()

    # Click cancel button
    checkout.click_cancel()

    # Wait and verify navigation back to cart
    WebDriverWait(driver, 10).until(EC.url_contains("cart"))
    assert "cart" in driver.current_url


# TC07 – Complete Full Checkout Flow (Main Test Case)
def test_complete_full_checkout_flow(driver):
    """
    Test: Complete end-to-end checkout process
    Flow: Login → Add 2 products → Cart → Checkout → Fill info → Continue → Finish
    """
    # Step 1: Login with correct credentials
    LoginPage(driver).login("standard_user", "secret_sauce")

    # Step 2: Add 2 products to cart
    products = ProductsPage(driver)
    products.add_products(2)
    assert products.get_cart_badge_count() == "2"

    # Step 3: Go to cart
    products.go_to_cart()
    cart = CartPage(driver)
    assert cart.get_cart_items_count() == 2

    # Step 4: Click checkout
    cart.click_checkout()
    checkout = CheckoutPage(driver)
    assert checkout.is_on_step_one()

    # Step 5: Fill checkout information (First Name, Last Name, Zip Code)
    checkout.fill_checkout_info("John", "Doe", "12345")

    # Step 6: Verify step two (overview page)
    assert checkout.is_on_step_two()

    # Step 7: Click finish button
    checkout.click_finish()

    # Step 8: Verify order success
    success_msg = checkout.get_success_message()
    assert "THANK YOU FOR YOUR ORDER" in success_msg.upper()
    assert "complete" in driver.current_url


# TC08 – Verify Checkout Overview Details
def test_checkout_overview_details(driver):
    """Test: Verify product details on checkout overview page"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Fill info and go to step two
    checkout.fill_checkout_info("Test", "User", "12345")
    assert checkout.is_on_step_two()

    # Verify 2 items are shown in overview
    from selenium.webdriver.common.by import By
    items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items) == 2


# TC09 – Back Home after order completion
def test_back_home_after_checkout(driver):
    """Test: Back home button returns to inventory"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Complete checkout
    checkout.fill_checkout_info("Test", "User", "12345")
    assert checkout.is_on_step_two()

    checkout.click_finish()

    # Click back home button
    checkout.click_back_home()

    # Wait and verify navigation to inventory
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url


# TC10 – Cancel from Step Two (Overview)
def test_cancel_checkout_from_overview(driver):
    """Test: Cancel button on overview page returns to inventory"""
    navigate_to_checkout(driver)
    checkout = CheckoutPage(driver)

    # Get to step two
    checkout.fill_checkout_info("Test", "User", "12345")
    assert checkout.is_on_step_two()

    # Click cancel from overview
    checkout.click_cancel()

    # Should return to inventory page
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

