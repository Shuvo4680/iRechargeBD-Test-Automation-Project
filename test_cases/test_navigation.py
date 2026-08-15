import pytest
from pages.home_page import HomePage
from utilities.read_properties import get


@pytest.mark.parametrize(
    "config_key",
    ["login_url", "signup_url", "api_docs_url", "package_plan_url", "about_url", "contact_url"],
)
def test_key_pages_are_reachable(driver, config_key):
    """Smoke-check that each key page in config.ini loads without error."""
    url = get("BASE", config_key)
    driver.get(url)
    assert driver.current_url is not None
    assert "error" not in driver.title.lower()


def test_homepage_has_nav_links(driver):
    home = HomePage(driver)
    home.load(get("BASE", "base_url"))

    hrefs = home.get_nav_link_hrefs()
    assert len(hrefs) > 0, "Expected at least one navigable link in the header/nav"
