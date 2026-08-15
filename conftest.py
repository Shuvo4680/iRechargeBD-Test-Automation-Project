import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    if os.getenv("HEADLESS", "").lower() in {"1", "true", "yes", "on"}:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
    )
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    from utilities.read_properties import get
    return get("BASE", "base_url", fallback="https://www.irechargebd.com/")
