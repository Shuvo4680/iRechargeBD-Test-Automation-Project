from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # --- Locators ---
    # NOTE: These are best-effort selectors based on the current public
    # markup of irechargebd.com. Re-verify with browser devtools if the
    # site's front end changes.
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand, header a[href='https://www.irechargebd.com']")
    NAV_LINKS = (By.CSS_SELECTOR, "nav a, header a")
    HERO_HEADING = (By.XPATH, "//h1[contains(., 'Mobile Recharge API')]")
    GET_STARTED_BTN = (By.XPATH, "//a[contains(text(), 'Get Started')]")
    VIEW_DOCS_BTN = (By.XPATH, "//a[contains(text(), 'View Docs')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Login')]")
    SIGNUP_LINK = (By.XPATH, "//a[contains(text(), 'Sign Up')]")
    OPERATOR_LOGOS = (By.CSS_SELECTOR, "img[src*='icons/']")
    OPERATOR_SECTION_HEADINGS = (By.XPATH, "//h3[contains(@class,'') and (contains(text(),'Grameenphone') or contains(text(),'Robi') or contains(text(),'Banglalink') or contains(text(),'Airtel') or contains(text(),'Teletalk'))]")
    FOOTER = (By.TAG_NAME, "footer")

    def load(self, base_url: str):
        self.open(base_url)

    def get_title(self) -> str:
        return self.driver.title

    def get_hero_heading_text(self) -> str:
        return self.get_text(self.HERO_HEADING)

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def click_signup(self):
        self.click(self.SIGNUP_LINK)

    def operator_logo_count(self) -> int:
        return len(self.find_all(self.OPERATOR_LOGOS))

    def is_footer_displayed(self) -> bool:
        return self.is_displayed(self.FOOTER)

    def get_nav_link_hrefs(self) -> list:
        elements = self.find_all(self.NAV_LINKS)
        return [el.get_attribute("href") for el in elements if el.get_attribute("href")]
