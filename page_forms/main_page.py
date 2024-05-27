from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator_constants import LocatorConstants
from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm

from utils.settings_data import SettingsData


class MainPage(BaseForm):
    __page_name = "Welcome to the-internet"

    def __init__(self):
        super(MainPage, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__page_name)), self.__page_name)

    @staticmethod
    def get_navigation_link_by_string(navigation):
        xpath = LocatorConstants.PRECISE_TEXT_XPATH.format(navigation)
        _element = PyQualityServices.element_factory
        print(f"Looking for navigation link with XPath: {xpath}")
        element = _element.get_link((By.XPATH, xpath), "Element for navigation")
        if element:
            print(f"Found element for navigation: {navigation}")
        else:
            print(f"Element for navigation '{navigation}' not found")
        return element

    def click_navigation_link_string(self, navigation):
        element = self.get_navigation_link_by_string(navigation)
        if element:
            element.click()
            print(f"Clicked on navigation link: {navigation}")
            # Wait for the URL to change indicating page navigation
            WebDriverWait(PyQualityServices.get_browser(), 10).until(
                EC.url_changes(SettingsData.get_env_data()['host'])
            )
            print(f"Current URL after click: {PyQualityServices.get_browser().current_url}")
        else:
            raise ValueError(f"Navigation link '{navigation}' not found")
