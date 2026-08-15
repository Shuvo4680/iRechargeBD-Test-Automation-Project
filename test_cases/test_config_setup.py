from utilities.read_properties import get, get_credentials


def test_config_base_url_is_set():
    base_url = get("BASE", "base_url")
    assert base_url and base_url.startswith("https://")


def test_config_timeouts_are_numeric():
    implicit_wait = get("TIMEOUTS", "implicit_wait")
    explicit_wait = get("TIMEOUTS", "explicit_wait")
    assert implicit_wait.isdigit()
    assert explicit_wait.isdigit()


def test_credentials_resolve_without_error():
    email, password = get_credentials()
    assert email is not None
    assert password is not None
