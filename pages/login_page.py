from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # --- Locators (best-effort, verify against live DOM) ---
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email'], input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(translate(text(),'LOGIN','login'),'login')] | //input[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger, .invalid-feedback, .error-message")
    DASHBOARD_INDICATOR = (By.XPATH, "//*[contains(text(),'Dashboard') or contains(text(),'Logout')]")

    def load(self, login_url: str):
        self.open(login_url)

    def login(self, email: str, password: str):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_displayed(self.ERROR_MESSAGE)

    def is_login_successful(self) -> bool:
        return self.is_displayed(self.DASHBOARD_INDICATOR)
