import os
from tenacity import retry, stop_after_delay, wait_fixed
from framework.utils.settings_data import SettingsData


class FileUtil:
    @staticmethod
    @retry(stop=stop_after_delay(SettingsData.get_env_data()['wait']), wait=wait_fixed(1))
    def is_file_exists(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return True
