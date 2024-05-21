from enum import Enum


class MainPageNavigation(Enum):
    ADD_REMOVE = "Add/Remove Elements"
    JAVASCRIPT_ALERT = "JavaScript Alerts"
    SORTABLE_DATA_TABLES = "Sortable Data Tables"
    DYNAMIC_CONTROLS = "Dynamic Controls"
    FILE_DOWNLOAD = "File Download"
    FILE_UPLOAD = "File Upload"
    BASIC_AUTH = "Basic Auth"

    @property
    def label(self):
        return self.value
