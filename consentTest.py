# AccuWeather Test in Python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from baseTest import TestBase, AssertionOutputHandler
import time


class TestConsentData(TestBase):
    policy_accept = (By.XPATH, f"//*[contains(@class, 'policy-accept')]")
    search_input = (By.XPATH, "//input[contains(@class,'search-input')]")
    selected_city = (By.XPATH, "//h1[contains(@class,'header-loc')]")
    search_bar_result = (By.XPATH, "//p[contains(@class,'search-bar-result__name')]")
    city_name = "New York City"

    def test_inserting_data_in_text_field(self, setup_teardown):
        # part1 of final assessment
        policy_button = self.wait.until(ec.element_to_be_clickable(self.policy_accept))
        policy_button.click()

        # part2 of final assessment
        search_box = self.wait.until(ec.element_to_be_clickable(self.search_input))
        AssertionOutputHandler.print_assertion_output("Search box found", bool(search_box))
        assert search_box, "Search box was not found"
        search_box.send_keys(self.city_name)

        # part3 of final assessment
        search_result = self.wait.until(
            ec.presence_of_element_located(self.search_bar_result))
        AssertionOutputHandler.print_assertion_output("Search result found", bool(search_result))
        assert search_result, "Search result was not found"
        search_result.click()
        time.sleep(5)

        city_name = self.wait.until(ec.visibility_of_element_located(self.selected_city))
        city_name_text = city_name.text.split(",")[0].strip()
        AssertionOutputHandler.print_assertion_output("City name matched", city_name_text == self.city_name)
        assert city_name_text == self.city_name, "City name didn't match"
