from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from framework.utils.settings_data import SettingsData
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstants


class DownloadPdfForm(BaseForm):
    __form_name = "Download as PDF"
    __element = PyQualityServices.element_factory
    __pdf_title = __element.get_label((By.XPATH,("//div[contains(@class, 'mw-electronpdfservice-selection-label-desc')]")),"File name")
    __download_btn = __element.get_button(
        (By.XPATH, ("//button[contains(@class, 'oo-ui-inputWidget-input')]")), "Download button")

    def __init__(self):
        super(DownloadPdfForm, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)), self.__form_name)


    def click_download_btn(self):
        return self.__download_btn.click()

    def is_file_download_link_displayed(self, name):
        return self.__pdf_title.state.is_displayed


