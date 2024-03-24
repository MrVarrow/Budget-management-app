from MobileAppWindow.MobileAppWindowModel import MobileAppWindowsModel
from MobileAppWindow.MobileAppWindowView import MobileAppWindowView


class MobileAppWindowController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.mobile_app_window_view = MobileAppWindowView(self.root, self)
        self.mobile_app_window_model = MobileAppWindowsModel()

    # Copy link when user press the button
    def copy_link(self, link):
        self.mobile_app_window_model.copy_app_link(link)

    # Sending email when user press the button
    def send_email_with_link(self, link):
        self.mobile_app_window_model.send_email_with_link(link, self.user_data[1])
