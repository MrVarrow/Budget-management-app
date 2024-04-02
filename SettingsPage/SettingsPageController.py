from SettingsPage.SettingsPageView import SettingsPageView
from SettingsPage.SettingsPageModel import SettingsPageModel
from tkinter import messagebox


class SettingsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.settings_page_view = SettingsPageView(self.root, self, self.bg_color)
        self.settings_page_model = SettingsPageModel()

    def support_and_help(self):
        # Create a chatbot with database in json which predict the best answer with disclaimer if anwer dont match issue send us email
        ...

    # Display info to user about version
    def app_version(self):
        messagebox.showinfo(title="Information", message="Current app version: Alpha 1.0")

    # Credits window popup
    def credits(self):
        self.settings_page_view.credits_window_create()

    def about_app(self):
        # Here show an app description
        ...

    # Change bg of app to dark or back to light based on choice
    def dark_mode(self):
        self.bg_color = self.settings_page_view.bg_color_change()

    # Go back to logged user page
    def back(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        self.settings_page_view.destroy_setting_page_frame()
        LoggedUserPageController(self.root, self.user_data, self.bg_color)

    # Credits window methods
    def credits_github(self, url):
        self.settings_page_model.credits_github_link(url)

    def credits_linkedin(self, url):
        self.settings_page_model.credits_linkedin_link(url)
