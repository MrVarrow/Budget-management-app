from CreateAccountPage.CreateAccountModel import CreateAccountPageModel
from CreateAccountPage.CreateAccountView import CreateAccountPageView
from tkinter import messagebox
from email_validator import EmailNotValidError


class CreateAccountPageController:
    def __init__(self, root):
        self.root = root
        self.create_account_view = CreateAccountPageView(self.root, self)
        self.create_account_model = CreateAccountPageModel()

    # Not sure about this rn
    def __call__(self, user_data, password_input, repeat_password_input):

        self.create_account_view.destroy_create_account_frame()
        from AccountPage.AccountPageController import AccountPageController
        AccountPageController(self.root, user_data)
        if self.password_validate(password_input) and self.repeat_password_validate(password_input, repeat_password_input):
            return True
        return False



    '''
    Check all conditions combined and if all is correct create account and sent confirm email, then going back to 
    login page 
    '''
    def create_account(self, login_input, password_input, repeat_password_input, email_input, notifications):
        if self.login_validate(login_input) and \
                self.password_validate(password_input) and \
                self.repeat_password_validate(password_input, repeat_password_input) and \
                self.email_validate(email_input):

            self.create_account_model.insert_user_to_database(login_input, password_input, email_input, notifications)
            self.create_account_model.account_created_successfully_email(email_input)
            self.create_account_view.destroy_create_account_frame()

            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
            messagebox.showinfo(title="Information", message="Your account has been created, now you can login")

    # Check if login meets requirements
    def login_validate(self, login_input):
        if not self.create_account_model.check_login_length(login_input):
            messagebox.showerror(title='Error', message="Your login is too short.")
            return False
        if not self.create_account_model.check_user_in_database(login_input):
            messagebox.showerror(title='Error', message="This login already exists, try again")
            return False
        return True

    # Check if password meets requirements
    def password_validate(self, password_input):
        if not self.create_account_model.check_password_length(password_input):
            messagebox.showerror(title='Error', message="Your password is too short.")
            return False
        if not self.create_account_model.check_password_for_small_char(password_input):
            messagebox.showerror(title='Error', message="Your password is missing small letter.")
            return False
        if not self.create_account_model.check_password_for_upper_char(password_input):
            messagebox.showerror(title='Error', message="Your password is missing large letter.")
            return False
        if not self.create_account_model.check_password_for_numbers(password_input):
            messagebox.showerror(title='Error', message="Your password is missing digit.")
            return False
        if not self.create_account_model.check_password_for_special_char(password_input):
            messagebox.showerror(title='Error', message="Your password is missing special character.")
            return False
        return True

    # Check if passwords are the same
    def repeat_password_validate(self, password_input, repeat_password_input):
        if not self.create_account_model.check_if_passwords_are_the_same(password_input, repeat_password_input):
            messagebox.showerror(title='Error', message="Passwords are not the same")
            return False
        return True

    # Check if email is valid
    def email_validate(self, email_input):
        if not self.create_account_model.check_email_in_database(email_input):
            messagebox.showerror(title='Error', message="This email already exists, try logging in")
            return False
        try:
            self.create_account_model.check_if_email_is_valid(email_input)
        except EmailNotValidError as e:
            messagebox.showerror(title='Error', message=str(e))
            return False
        return True

    # Display question if user wants to go back to login page, then takes action based on decision
    def back(self):
        result = messagebox.askquestion(title='Warning', message="Do you want go back to Login page?")
        if result == "yes":
            # this import look strange for me. I cannot find other way to make this work because of circular import error
            self.create_account_view.destroy_create_account_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
        elif result == "no":
            pass
