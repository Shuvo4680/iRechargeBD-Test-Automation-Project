from pages.login_page import LoginPage
from utilities.read_properties import get, get_credentials
from utilities.excel_utils import read_csv


def test_login_with_invalid_credentials_shows_error(driver):
    """
    Uses intentionally invalid credentials — this project does not
    attempt to log in with real account credentials against a live
    production site.
    """
    login = LoginPage(driver)
    login.load(get("BASE", "login_url"))

    login.login("invalid_user@example.com", "WrongPassword1")

    assert login.is_error_displayed() or not login.is_login_successful()
    login.take_screenshot("login_result")


def test_login_data_driven(driver):
    """Data-driven pass using test_data/users.csv."""
    users = read_csv("users.csv")
    login = LoginPage(driver)

    for user in users:
        login.load(get("BASE", "login_url"))
        login.login(user["email"], user["password"])
        if user["expected_result"] == "fail":
            assert not login.is_login_successful()
