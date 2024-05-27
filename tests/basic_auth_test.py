import pytest
from browser.py_quality_services import PyQualityServices
from page_forms.basic_auth import BasicAuth
from page_forms.main_page import MainPage
from utils.settings_data import SettingsData
from tests.base_test import prepare_browser_factory


class TestBasicAuth:
    @pytest.fixture(scope="class")
    def main_page(self, prepare_browser_factory):
        return MainPage()

    @pytest.fixture(scope="class")
    def basic_auth_page(self, prepare_browser_factory):
        return BasicAuth()

    @pytest.fixture(autouse=True)
    def setup_auth(self, prepare_browser_factory):
        settings = SettingsData()
        self.domain = settings.get_env_data()['domain']
        self.username = settings.get_user_data()['username']
        self.password = settings.get_user_data()['password']

    def test_basic_auth(self, main_page, basic_auth_page):
        main_page.click_navigation_link_string("Basic Auth")

        basic_auth_url = f"https://{self.username}:{self.password}@{self.domain}/basic_auth"
        PyQualityServices.get_browser().go_to(basic_auth_url)
        assert basic_auth_page.is_success_msg_displayed(), "Success message was not displayed"
