from pages.login_page import LoginPage


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "wrong_password")

    assert login.is_error_displayed()
    assert "inventory" not in driver.current_url
