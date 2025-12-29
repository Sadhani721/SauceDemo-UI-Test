from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_positive_purchase_flow(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.sort_low_to_high()
    products.add_items_to_cart(2)

    assert products.get_cart_count() == "2"

    products.go_to_cart()
    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("John", "Doe", "12345")
    checkout.click_finish()

    assert checkout.get_success_message() == "Thank you for your order!"

