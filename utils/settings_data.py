import json
import logging


class SettingsData:
    RESOURCE_FILE_PATH = "../resources/"
    ENV_FILE_PATH = RESOURCE_FILE_PATH + "env.json"
    PROD_FILE_PATH = RESOURCE_FILE_PATH + "prod.json"
    USER_FILE_PATH = RESOURCE_FILE_PATH + "userData.json"
    DATA_TABLE_FILE_PATH = RESOURCE_FILE_PATH + "dataTableData.json"
    FILE_DATA_PATH = RESOURCE_FILE_PATH + "fileData.json"
    ERROR_MSG = "File with environment settings not found or incorrect"
    ERROR_FILE_READ_MSG = "Environment file not found"

    @staticmethod
    def get_environment():
        try:
            with open(SettingsData.ENV_FILE_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_MSG)
            raise

    @staticmethod
    def get_env_data():
        try:
            if SettingsData.get_environment()['env'] == "prod":
                with open(SettingsData.PROD_FILE_PATH, 'r') as f:
                    return json.load(f)
            logging.info("Env is not set")
            raise RuntimeError(SettingsData.ERROR_MSG)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_FILE_READ_MSG + " at: " + SettingsData.PROD_FILE_PATH)
            raise

    @staticmethod
    def get_user_data():
        try:
            with open(SettingsData.USER_FILE_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_MSG)
            raise RuntimeError(SettingsData.ERROR_MSG)

    @staticmethod
    def get_data_table_data():
        try:
            with open(SettingsData.DATA_TABLE_FILE_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(SettingsData.ERROR_MSG)
            raise RuntimeError(SettingsData.ERROR_MSG)
