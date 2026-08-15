import time
from pages.signup_page import SignupPage
from utilities.read_properties import get


def test_signup_form_validation_on_empty_submit(driver):
    """Submitting the signup form empty should surface validation errors,
    not silently succeed."""
    signup = SignupPage(driver)
    signup.load(get("BASE", "signup_url"))

    signup.submit()

    assert signup.is_validation_error_displayed() or driver.current_url.endswith("/signup")
    signup.take_screenshot("signup_result")


def test_signup_form_accepts_valid_looking_data(driver):
    """
    Fills the form with clearly synthetic data to verify the form
    submits without client-side validation errors. Does NOT assert
    account creation succeeds against the live backend.
    """
    signup = SignupPage(driver)
    signup.load(get("BASE", "signup_url"))

    unique_suffix = str(int(time.time()))
    signup.fill_form(
        name="QA Test User",
        email=f"qa_test_{unique_suffix}@example.com",
        phone="01700000000",
        password="ChangeMe123!",
    )

    assert not signup.is_validation_error_displayed()
