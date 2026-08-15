import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")
LOCAL_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.local.ini")


def read_config():
    """
    Reads config/config.ini, then overlays config/config.local.ini
    if present (git-ignored, for local secrets/overrides).
    """
    parser = configparser.ConfigParser()
    parser.read(CONFIG_PATH)
    if os.path.exists(LOCAL_CONFIG_PATH):
        parser.read(LOCAL_CONFIG_PATH)
    return parser


def get(section: str, key: str, fallback=None):
    config = read_config()
    return config.get(section, key, fallback=fallback)


def get_credentials():
    """
    Prefer environment variables over config.ini for credentials.
    """
    email = os.getenv("IRECHARGE_EMAIL") or get("CREDENTIALS", "email")
    password = os.getenv("IRECHARGE_PASSWORD") or get("CREDENTIALS", "password")
    return email, password
