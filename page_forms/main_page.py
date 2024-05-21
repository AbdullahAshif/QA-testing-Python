from locator_constants import LocatorConstants
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices
from .main_page_navigation import MainPageNavigation
from forms.base_form import BaseForm


class MainPage(BaseForm):

    def __init__(self, driver):
        self.driver = driver
        locator = (By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format("Welcome to the-internet"))
        name = "Main Page"
        super().__init__(locator, name)

    def is_displayed(self):
        return self.driver.find_element(By.TAG_NAME, 'body').is_displayed()

    @staticmethod
    def get_navigation_link_by_enum(navigation: MainPageNavigation):
        return PyQualityServices.element_factory.get_link(By.XPATH,
                                                          LocatorConstants.PRECISE_TEXT_XPATH.format(navigation.label),
                                                          navigation.label)

    @staticmethod
    def get_navigation_link_by_string(navigation: str):
        return PyQualityServices.element_factory.get_link(By.XPATH,
                                                          LocatorConstants.PRECISE_TEXT_XPATH.format(navigation),
                                                          "Element for navigation")

    def click_navigation_link_enum(self, navigation: MainPageNavigation):
        self.get_navigation_link_by_enum(navigation).click()

    def click_navigation_link_string(self, navigation_link: str):
        self.get_navigation_link_by_string(navigation_link).click()
