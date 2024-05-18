import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class TestBase:
    _url = "https://www.accuweather.com/"
    _max_wait = 30

    @pytest.fixture
    def setup_teardown(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, self._max_wait)
        self.driver.maximize_window()
        self.driver.get(self._url)
        yield
        self.driver.quit()


class AssertionOutputHandler:
    @staticmethod
    def print_assertion_output(assertion_description, assertion_result):
        print(f"\nAssertion: {assertion_description}")
        if not assertion_result:
            print("Assertion failed!")
        else:
            print("Assertion passed!")
