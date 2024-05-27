import pytest
from browser.py_quality_services import PyQualityServices

from page_forms.main_page import MainPage
from utils.settings_data import SettingsData


@pytest.fixture(scope="session", autouse=True)
def prepare_browser_factory(request):
    driver = PyQualityServices.get_browser()  # Assuming PyQualityServices provides a WebDriver instance
    driver.maximize()
    driver.go_to(SettingsData.get_env_data()['host'])
    driver.wait_for_page_to_load()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def main_page(prepare_browser_factory):
    return MainPage()
