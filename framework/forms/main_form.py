from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from framework.locator_constants import LocatorConstants
from framework.utils.settings_data import SettingsData


class MainForm(BaseForm):
    __form_name = "WIKIPEDIA"
    _element = PyQualityServices.element_factory
    _browser = PyQualityServices.get_browser()
    __search_input = (By.XPATH, "//*[contains(@id,'searchInput')]")
    __submit = (By.XPATH, "//*[contains(@class,'svg-search-icon')]")
    __search_field = _element.get_text_box(__search_input, "Search Field")
    __submit_btn = _element.get_button(__submit, "Submit Button")

    def __init__(self):
        super(MainForm, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)), self.__form_name)

    @classmethod
    def get_navigation_link(cls, navigation):
        xpath = LocatorConstants.PRECISE_TEXT_XPATH.format(navigation)
        print(f"Looking for navigation link with XPATH: {xpath}")
        element = cls._element.get_link((By.XPATH, xpath), "Element for navigation")
        if element:
            print(f"Found element for navigation '{navigation}'")
        else:
            print(f"Element for navigation '{navigation}' not found")
        return element

    def click_navigation_link(self, navigation):
        element = self.get_navigation_link(navigation)
        if element:
            print(f"Clicked on navigation link: {navigation}")
            WebDriverWait(self._browser, 10).until(
                ec.url_changes(SettingsData.get_env_data()['host'])
            )
            print(f"Current URL after click: {self._browser.current_url}")
        else:
            raise ValueError(f"Navigation link '{navigation}' not found")

    def click_submit_btn(self):
        self.__submit_btn.click()

    def input_text(self, text):
        self.__search_field.clear_and_type(text)

    def is_submit_btn_clickable(self):
        return self.__submit_btn.state.is_clickable

    def is_displayed(self):
        return self.state.wait_for_not_displayed
    