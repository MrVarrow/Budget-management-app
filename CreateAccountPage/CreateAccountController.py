from CreateAccountPage.CreateAccountModel import CreateAccountPageModel
from CreateAccountPage.CreateAccountView import CreateAccountPageView
from tkinter import messagebox


class CreateAccountPageController:
    def __init__(self, root):
        self.root = root
        self.create_account_model = CreateAccountPageModel()
        self.create_account_view = CreateAccountPageView(self.root, self)

    def create_account(self):
        ...

    # Display question if user wants to go back to login page, then takes action based on decision
    def back(self):
        result = messagebox.askquestion(title='Warning', message="Do you want go back to Login page?")
        if result == "yes":
            # this import look strange for me but i cannot find other way to make this work because of circular import error
            self.create_account_view.destroy_create_account_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
        elif result == "no":
            pass

    def email_notifications(self):
        ...

