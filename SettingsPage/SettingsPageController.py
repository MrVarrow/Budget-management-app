from SettingsPage.SettingsPageView import SettingsPageView
from SettingsPage.SettingsPageModel import SettingsPageModel


class SettingsPageController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.settings_page_view = SettingsPageView(self.root, self)
        self.settings_page_model = SettingsPageModel()
