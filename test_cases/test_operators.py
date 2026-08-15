from pages.operators_page import OperatorsPage
from utilities.read_properties import get


def test_all_expected_operators_are_listed(driver):
    operators = OperatorsPage(driver)
    operators.load(get("BASE", "base_url"))

    visible = operators.get_visible_operator_names()
    missing = set(OperatorsPage.EXPECTED_OPERATORS) - set(visible)

    assert not missing, f"Missing expected operators on homepage: {missing}"
