from locator_constants import LocatorConstants
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm


class BasicAuthPage(BaseForm):
    __page_name = "JavaScript Alerts"
    _element = PyQualityServices.element_factory
    __success_msg = _element.get_label((By.XPATH,
                                        LocatorConstants.PARTICULAR_TEXT_XPATH.format(
                                            "Congratulations! You must have the proper credentials.")),
                                       "Success message text")

    def __init__(self):
        super(BasicAuthPage, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__page_name)),
                                        self.__page_name)

    def is_success_msg_displayed(self):
        return self.__success_msg.state.is_displayed
