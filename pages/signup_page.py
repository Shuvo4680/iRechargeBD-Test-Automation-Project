from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):
    # --- Locators (best-effort, verify against live DOM) ---
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name'], input[name='full_name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email'], input[type='email']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[name='phone'], input[type='tel']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='confirm_password'], input[name='password_confirmation']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(translate(text(),'SIGN UP','sign up'),'sign up') or @type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success, .success-message")
    VALIDATION_ERROR = (By.CSS_SELECTOR, ".alert-danger, .invalid-feedback")

    def load(self, signup_url: str):
        self.open(signup_url)

    def fill_form(self, name: str, email: str, phone: str, password: str):
        if self.is_displayed(self.NAME_INPUT):
            self.type_text(self.NAME_INPUT, name)
        self.type_text(self.EMAIL_INPUT, email)
        if self.is_displayed(self.PHONE_INPUT):
            self.type_text(self.PHONE_INPUT, phone)
        self.type_text(self.PASSWORD_INPUT, password)
        if self.is_displayed(self.CONFIRM_PASSWORD_INPUT):
            self.type_text(self.CONFIRM_PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def is_success_displayed(self) -> bool:
        return self.is_displayed(self.SUCCESS_MESSAGE)

    def is_validation_error_displayed(self) -> bool:
        return self.is_displayed(self.VALIDATION_ERROR)
