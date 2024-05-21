import pytest
from browser.py_quality_services import PyQualityServices
from page_forms.main_page import MainPage
from page_forms.main_page_navigation import MainPageNavigation
from utils.browser_factory import BrowserFactory
from utils.settings_data import SettingsData


@pytest.fixture(scope="session", autouse=True)
def prepare_browser_factory(request):
    PyQualityServices.browser_factory = BrowserFactory()
    browser = PyQualityServices.get_browser()
    browser.maximize()
    browser.go_to(SettingsData.get_env_data().get_host())
    yield browser
    browser.quit()


@pytest.fixture(scope="class")
def main_page(prepare_browser_factory):
    return MainPage(driver=prepare_browser_factory)


@pytest.mark.usefixtures("main_page")
class TestSiteAccess:
    def test_site_access(self, main_page):
        assert main_page.is_displayed(), "Main page is not displayed"

    def test_navigation_add_remove_elements(self, main_page):
        main_page.click_navigation_link_enum(MainPageNavigation.ADD_REMOVE)
        assert "add_remove_elements" in main_page.driver.current_url, "Failed to navigate to Add/Remove Elements page"

    def test_navigation_file_upload(self, main_page):
        main_page.click_navigation_link_enum(MainPageNavigation.FILE_UPLOAD)
        assert "upload" in main_page.driver.current_url, "Failed to navigate to File Upload page"

    def test_navigation_basic_auth(self, main_page):
        main_page.click_navigation_link_enum(MainPageNavigation.BASIC_AUTH)
        assert "basic_auth" in main_page.driver.current_url, "Failed to navigate to Basic Auth page"
