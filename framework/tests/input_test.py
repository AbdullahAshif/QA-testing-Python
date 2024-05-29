import pytest
import os

from framework.forms.main_form import MainForm
from framework.forms.searched_form import SearchedForm
from framework.forms.download_pdf_form import DownloadPdfForm
from framework.utils.file_util import FileUtil
from framework.utils.settings_data import SettingsData
from framework.tests.base_test import prepare_browser_factory
from framework.utils.file_util import FileUtil


class TestInput:
    __file_name = SettingsData.get_file_data()['downloadFile']
    __file_path = os.path.join(SettingsData.DOWNLOAD_DIR, __file_name)
    __search_value = SettingsData.get_search_value()['searchValue']

    @pytest.fixture(scope="class")
    def main_form(self, prepare_browser_factory):
        return MainForm()

    @pytest.fixture(scope="class")
    def search_form(self, prepare_browser_factory):
        return SearchedForm()

    @pytest.fixture(scope="class")
    def download_form(self, prepare_browser_factory):
        return DownloadPdfForm()

    def test_input(self, main_form, search_form, download_form):
        assert main_form.is_displayed(), "Main page is not displayed"

        main_form.input_text(self.__search_value)
        assert main_form.is_submit_btn_clickable(), "Submit button is not clickable"

        main_form.click_submit_btn()
        assert search_form.click_tools_checkbox(), "Tools button is not clickable"
        assert search_form.is_click_download_pdf_option_clickable(), "Download button is not clickable"

        search_form.click_tools_checkbox()
        download_form.click_download_btn()

        assert FileUtil.is_file_exists(self.__file_path), "File is not downloaded"
