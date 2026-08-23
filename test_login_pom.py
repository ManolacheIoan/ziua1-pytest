from pages.login_page import LoginPage


def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area" in login_page.get_success_message()


def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid" in login_page.get_error_message()