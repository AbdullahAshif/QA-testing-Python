from locator_constants import LocatorConstants
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices
from forms.base_form import BaseForm


class AlertPage(BaseForm):
    __page_name = "JavaScript Alerts"
    _element = PyQualityServices.element_factory
    __click_js_alert_btn = _element.get_button(LocatorConstants.JS_ALERT_BTN_LOCATOR,
                                               "Click for JS Alert btn")
    __success_message_lbl = _element.get_label(
        (By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format("You successfully clicked an alert")),
        "Success message text")

    def __init__(self):
        super(AlertPage, self).__init__((By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__page_name)),
                                        self.__page_name)

    def click_js_alert_btn(self):
        self.__click_js_alert_btn.click()

    def is_success_message_displayed(self):
        return self.__success_message_lbl.state.is_displayed