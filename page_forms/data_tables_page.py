from locator_constants import LocatorConstants
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm


class DataTablesPage(BaseForm):
    __page_name = "Data Tables"
    _element = PyQualityServices.element_factory
    __due_locator = (By.XPATH, "//*[@id='table1']//td[4]")

    def __init__(self):
        super(DataTablesPage, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__page_name)),
                                             self.__page_name)

    def get_first_due_list(self):
        due_list = []
        for label in self._get_first_due_lbl_list():
            due_list.append(label.text)
        return due_list

    def _get_first_due_lbl_list(self):
        return self._element.find_elements(self.__due_locator, "due", "label")
