from selenium.webdriver.common.by import By
from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.elements.states.element_state_provider import ElementStateProvider

from framework.locator_constants import LocatorConstants


class SearchedForm(BaseForm):
    __element_factory = PyQualityServices.element_factory
    __browser = PyQualityServices.get_browser()
    __tool_btn = PyQualityServices.element_factory.get_button(
        (By.XPATH, ("//*[@id='vector-page-tools-dropdown']")), "Click tools")
    __download_lbl = PyQualityServices.element_factory.get_button(
        (By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format("Download as PDF")), "Click Download as PDF")

    def __init__(self):
        super(SearchedForm, self).__init__((By.ID, "firstHeading"), "Albert Einstein Page")

    def click_tools_checkbox(self):
        self.__tool_btn.state.wait_for_clickable()
        self.__tool_btn.click()
        return True  # Return True to indicate success

    def is_click_download_pdf_option_clickable(self):
        self.__download_lbl.state.wait_for_clickable()
        try:
            self.__download_lbl.click()
            return True  # Return True to indicate the click was successful
        except Exception as e:
           print(f"An error occurred: {e}")
        return False  # Return False if an error occurs during the click
