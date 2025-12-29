from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_debug_checkout_flow(driver):
    """Debug test to see what's happening step by step"""
    print(f"\n1. Initial URL: {driver.current_url}")

    # Step 1: Login
    LoginPage(driver).login("standard_user", "secret_sauce")
    time.sleep(1)
    print(f"2. After login URL: {driver.current_url}")

    # Step 2: Add products
    products = ProductsPage(driver)
    products.add_products(2)
    time.sleep(1)
    print(f"3. After adding products URL: {driver.current_url}")

    # Step 3: Go to cart
    products.go_to_cart()
    time.sleep(1)
    print(f"4. After going to cart URL: {driver.current_url}")

    # Step 4: Go to checkout
    CartPage(driver).click_checkout()
    time.sleep(1)
    print(f"5. After clicking checkout URL: {driver.current_url}")

    # Step 5: Fill checkout info
    checkout = CheckoutPage(driver)
    print(f"6. Is on step one: {checkout.is_on_step_one()}")

    # Manually fill form and click continue
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)

    print(f"7. Before clicking continue URL: {driver.current_url}")

    # Find and click continue button
    continue_btns = driver.find_elements(By.ID, "continue")
    print(f"8. Number of continue buttons found: {len(continue_btns)}")

    if continue_btns:
        continue_btn = continue_btns[0]
        print(f"9. Continue button is displayed: {continue_btn.is_displayed()}")
        print(f"10. Continue button is enabled: {continue_btn.is_enabled()}")
        print(f"11. Continue button value: {continue_btn.get_attribute('value')}")

        # Try to click
        try:
            continue_btn.click()
            time.sleep(2)
            print(f"12. After normal click URL: {driver.current_url}")
        except Exception as e:
            print(f"12. Error with normal click: {e}")
            # Try JS click
            try:
                driver.execute_script("arguments[0].click();", continue_btn)
                time.sleep(2)
                print(f"13. After JS click URL: {driver.current_url}")
            except Exception as e2:
                print(f"13. Error with JS click: {e2}")

    print(f"14. Is on step two: {checkout.is_on_step_two()}")

    # Take screenshot
    driver.save_screenshot("screenshots/debug_test.png")
    print("15. Screenshot saved to screenshots/debug_test.png")

