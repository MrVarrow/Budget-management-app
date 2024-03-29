from LoggedUserPage.LoggedUserPageView import LoggedUserPageView
from LoggedUserPage.LoggedUserPageModel import LoggedUserPageModel
from SettingsPage.SettingsPageController import SettingsPageController
from AccountPage.AccountPageController import AccountPageController
from RateAppWindow.RateAppWindowController import RateAppWindowController
from MobileAppWindow.MobileAppWindowController import MobileAppWindowController

from tkinter import messagebox


class LoggedUserPageController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.logged_user_page_view = LoggedUserPageView(self.root, self)
        self.logged_user_page_model = LoggedUserPageModel()

    # Go into settings
    def settings(self):
        SettingsPageController(self.root, self.user_data)

    # Go into user account
    def your_acc(self):
        AccountPageController(self.root, self.user_data)

    # Go into manage budget page
    def manage_budget(self):
        ...

    # Go into statistics page
    def stats(self):
        ...

    # Go into shopping list page
    def shopping_list(self):
        ...

    # Go into savings page
    def savings(self):
        ...

    # Go into receipts page
    def receipts(self):
        ...

    # Go into rate us window
    def rate_us(self):
        RateAppWindowController(self.root, self.user_data)

    # Go into mobile app window
    def mobile_app(self):
        MobileAppWindowController(self.root, self.user_data)

    # Display question if user wants to log out, then takes action based on decision
    def logout(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to logout from Budget manager?")
        if result == "yes":
            # this import look strange for me but i cannot find other way to make this work because of circular import error
            self.logged_user_page_view.destroy_logged_user_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
        elif result == "no":
            pass

    # Display question if user wants to exit, then takes action based on decision
    def exit(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass
