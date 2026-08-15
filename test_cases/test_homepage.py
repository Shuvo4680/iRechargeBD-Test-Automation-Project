from pages.home_page import HomePage
from utilities.read_properties import get


def test_homepage_loads_and_title_is_correct(driver):
    home = HomePage(driver)
    home.load(get("BASE", "base_url"))

    assert "iRecharge" in home.get_title()
    home.take_screenshot("homepage_result")


def test_homepage_hero_heading_visible(driver):
    home = HomePage(driver)
    home.load(get("BASE", "base_url"))

    heading_text = home.get_hero_heading_text()
    assert "Mobile Recharge" in heading_text


def test_homepage_operator_logos_displayed(driver):
    home = HomePage(driver)
    home.load(get("BASE", "base_url"))

    logo_count = home.operator_logo_count()
    assert logo_count >= 5, f"Expected at least 5 operator logos, found {logo_count}"


def test_homepage_footer_displayed(driver):
    home = HomePage(driver)
    home.load(get("BASE", "base_url"))

    assert home.is_footer_displayed()
