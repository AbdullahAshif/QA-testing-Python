from typing import Tuple
from selenium.webdriver.common.by import By

class LocatorConstants:
    PRECISE_TEXT_XPATH = "//*[text()='{}']"
    PARTICULAR_TEXT_XPATH = "//*[contains(text(), '{}')]"
    JS_ALERT_BTN_LOCATOR: Tuple[By, str] = (By.XPATH, "//button[@onclick='jsAlert()']")
    BASIC_AUTH_MSG_LOCATOR: Tuple[By, str] = (By.XPATH, '//*[contains(@id, "content")]/div/p')
    DUE_LOCATOR: Tuple[By, str] = (By.XPATH, "//*[@id='table1']//td[4]")
