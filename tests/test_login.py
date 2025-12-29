from pages.login_page import LoginPage


# Valid Login

def test_login_valid_credentials(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


# Valid Username + Invalid Password

def test_login_valid_username_invalid_password(driver):
    login = LoginPage(driver)
    login.login("standard_user", "wrong_password")

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()


# Invalid Username + Valid Password

def test_login_invalid_username_valid_password(driver):
    login = LoginPage(driver)
    login.login("invalid_user", "secret_sauce")

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()


# Invalid Username + Invalid Password

def test_login_invalid_username_invalid_password(driver):
    login = LoginPage(driver)
    login.login("invalid_user", "wrong_password")

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()


# Empty Username + Empty Password

def test_login_empty_credentials(driver):
    login = LoginPage(driver)
    login.click_login()

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()


# Empty Username + Valid Password

def test_login_empty_username(driver):
    login = LoginPage(driver)
    login.login("", "secret_sauce")

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()


# Valid Username + Empty Password

def test_login_empty_password(driver):
    login = LoginPage(driver)
    login.login("standard_user", "")

    assert login.is_error_displayed()
    assert "Epic sadface" in login.get_error_message()