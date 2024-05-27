import pytest
from browser.alert_actions import AlertActions
from page_forms.alerts_page import AlertPage
from page_forms.main_page import MainPage
from browser.py_quality_services import PyQualityServices
from tests.base_test import prepare_browser_factory


class TestAlert:
    @pytest.fixture(scope="class")
    def main_page(self, prepare_browser_factory):
        return MainPage()

    @pytest.fixture(scope="class")
    def js_alert_page(self, prepare_browser_factory):
        return AlertPage()

    def test_alert(self, main_page, js_alert_page):
        main_page.click_navigation_link_string("JavaScript Alerts")
        js_alert_page.click_js_alert_btn()
        PyQualityServices.get_browser().handle_alert(AlertActions.ACCEPT)
        assert js_alert_page.is_success_message_displayed(), "Success message wasn't displayed"
