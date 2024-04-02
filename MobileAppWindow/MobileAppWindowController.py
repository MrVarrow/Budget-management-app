from MobileAppWindow.MobileAppWindowModel import MobileAppWindowsModel
from MobileAppWindow.MobileAppWindowView import MobileAppWindowView


class MobileAppWindowController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.mobile_app_window_view = MobileAppWindowView(self.root, self, self.bg_color)
        self.mobile_app_window_model = MobileAppWindowsModel()

    # Copy link when user press the button
    def copy_link(self, link):
        self.mobile_app_window_model.copy_app_link(link)

    # Sending email when user press the button
    def send_email_with_link(self, link):
        self.mobile_app_window_model.send_email_with_link(link, self.user_data[1])
