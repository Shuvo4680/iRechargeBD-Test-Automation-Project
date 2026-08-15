import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utilities.logger import get_logger
from utilities.read_properties import get

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.wait_time = int(get("TIMEOUTS", "explicit_wait", fallback=15))

    def open(self, url: str):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find(locator).text

    def is_displayed(self, locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    def wait_for_url_contains(self, fragment: str) -> bool:
        try:
            WebDriverWait(self.driver, self.wait_time).until(EC.url_contains(fragment))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name: str):
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved: {path}")
        return path
