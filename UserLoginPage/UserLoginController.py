from UserLoginPage.UserLoginView import UserLoginView
from UserLoginPage.UserLoginModel import UserLoginModel
from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
from CreateAccountPage.CreateAccountController import CreateAccountPageController
from tkinter import messagebox


class UserLoginController:
    def __init__(self, root, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.login_user_page_view = UserLoginView(self.root, self, self.bg_color)
        self.login_user_page_model = UserLoginModel()

    def user_login(self, login_input, password_input):
        # Check if user entered both login and password
        if login_input == '' or password_input == '':
            messagebox.showinfo(title="Information", message="Please enter both username and password.")
            return
        user_data = self.login_user_page_model.user_input_is_not_empty(login_input)

        # Check if user is registered
        if user_data is None:
            messagebox.showinfo(title="Information", message="User does not exist.")
            return
        password = user_data[2]

        # Check if password entered by user is correct
        if password == password_input:
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

    def forgot_pass(self, login_input):
        # Check if user entered a login
        if login_input == '':
            messagebox.showinfo(title="Information", message="Please enter username")
            return
        user_data = self.login_user_page_model.user_input_is_not_empty(login_input)

        # Check if user is registered
        if user_data is None:
            messagebox.showinfo(title="Information", message="User does not exist.")
            return
        self.login_user_page_model.email_with_password(user_data)
        messagebox.showinfo(title="Information", message="E-mail with password has been sent")

    # Go into create account page
    def create_acc(self):
        self.login_user_page_view.destroy_login_page_frame()
        CreateAccountPageController(self.root, self.bg_color)
