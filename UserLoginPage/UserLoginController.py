from UserLoginPage.UserLoginView import UserLoginView
from UserLoginPage.UserLoginModel import UserLoginModel
from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
from CreateAccountPage.CreateAccountController import CreateAccountPageController
from Validations.Validations import empty_string_inside_widget, variable_is_none, two_strings_are_the_same
from tkinter import messagebox


class UserLoginController:
    def __init__(self, root, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.login_user_page_view = UserLoginView(self.root, self, self.bg_color)
        self.login_user_page_model = UserLoginModel()

    def user_login(self, login_input: str, password_input: str):
        # Check if user entered both login and password
        if empty_string_inside_widget(login_input) or empty_string_inside_widget(password_input):
            messagebox.showinfo(title="Information", message="Please enter both username and password.")
            return
        user_data = self.login_user_page_model.get_user_data(login_input)

        # Check if user is registered
        if variable_is_none(user_data):
            messagebox.showinfo(title="Information", message="User does not exist.")
            return
        password = user_data[2]

        # Check if password entered by user is correct
        if two_strings_are_the_same(password, password_input):
            self.login_user_page_view.destroy_login_page_frame()
            LoggedUserPageController(self.root, user_data, self.bg_color)
        else:
            messagebox.showinfo(title="Information", message="Incorrect password.")

    # Display question if user wants to exit, then takes action based on decision
    def exit_from_app(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass

    def forgot_pass(self, login_input: str):
        # Check if user entered a login
        if empty_string_inside_widget(login_input):
            messagebox.showinfo(title="Information", message="Please enter username")
            return
        user_data = self.login_user_page_model.get_user_data(login_input)

        # Check if user is registered
        if variable_is_none(user_data):
            messagebox.showinfo(title="Information", message="User does not exist.")
            return
        self.login_user_page_model.email_with_password(user_data)
        messagebox.showinfo(title="Information", message="E-mail with password has been sent")

    # Go into create account page
    def create_acc(self):
        self.login_user_page_view.destroy_login_page_frame()
        CreateAccountPageController(self.root, self.bg_color)
