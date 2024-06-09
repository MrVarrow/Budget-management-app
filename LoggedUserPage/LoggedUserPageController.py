from LoggedUserPage.LoggedUserPageView import LoggedUserPageView
from LoggedUserPage.LoggedUserPageModel import LoggedUserPageModel
from SettingsPage.SettingsPageController import SettingsPageController
from AccountPage.AccountPageController import AccountPageController
from RateAppWindow.RateAppWindowController import RateAppWindowController
from MobileAppWindow.MobileAppWindowController import MobileAppWindowController
from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
from ShoppingListPage.ShoppingListController import ShoppingListController
from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
from tkinter import messagebox


class LoggedUserPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.logged_user_page_view = LoggedUserPageView(self.root, self, self.bg_color)
        self.logged_user_page_model = LoggedUserPageModel()

    # Go into settings
    def settings(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        SettingsPageController(self.root, self.user_data, self.bg_color)

    # Go into user account
    def your_acc(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        AccountPageController(self.root, self.user_data, self.bg_color)

    # Go into manage budget page
    def manage_budget(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)

    # Go into statistics page
    def stats(self):
        ...

    # Go into shopping list page
    def shopping_list(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ShoppingListController(self.root, self.user_data, self.bg_color)

    # Go into savings page
    def savings(self):
        ...

    # Go into receipts page
    def receipts(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ReceiptsPageController(self.root, self.user_data, self.bg_color)

    # Go into rate us window
    def rate_us(self):
        RateAppWindowController(self.root, self.user_data, self.bg_color)

    # Go into mobile app window
    def mobile_app(self):
        MobileAppWindowController(self.root, self.user_data, self.bg_color)

    # Display question if user wants to log out, then takes action based on decision
    def logout(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to logout from Budget manager?")
        if result == "yes":
            # this import look strange for me but i cannot find other way to make this work because of circular import error
            self.logged_user_page_view.destroy_logged_user_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root, self.bg_color)
        elif result == "no":
            pass

    # Display question if user wants to exit, then takes action based on decision
    def exit(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass
