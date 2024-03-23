from MobileAppWindow.MobileAppWindowModel import MobileAppWindowsModel
from MobileAppWindow.MobileAppWindowView import MobileAppWindowView


class MobileAppWindowController:
    def __init__(self, root, user_data):
        # maybe add option to sent e-mail with link to app
        self.root = root
        self.user_data = user_data
        self.mobile_app_window_view = MobileAppWindowView(self.root, self)
        self.mobile_app_window_model = MobileAppWindowsModel()
