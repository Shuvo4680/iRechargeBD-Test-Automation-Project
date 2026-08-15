from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OperatorsPage(BasePage):
    EXPECTED_OPERATORS = [
        "Grameenphone",
        "Robi",
        "Banglalink",
        "Airtel",
        "Teletalk",
    ]

    OPERATOR_NAME_HEADINGS = (By.XPATH, "//h3 | //h4")

    def load(self, base_url: str):
        self.open(base_url)

    def get_visible_operator_names(self) -> list:
        headings = self.find_all(self.OPERATOR_NAME_HEADINGS)
        texts = [h.text.strip() for h in headings if h.text.strip()]
        return [name for name in self.EXPECTED_OPERATORS if any(name in t for t in texts)]
