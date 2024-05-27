from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile

from utils.browser_factory import BrowserFactory


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()