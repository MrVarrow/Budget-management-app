from CreateAccountPage.CreateAccountModel import CreateAccountPageModel
from CreateAccountPage.CreateAccountView import CreateAccountPageView
from tkinter import messagebox
from email_validator import EmailNotValidError
from Validations.Validations import length_of_string_more_equal_than, lower_char_in_string, upper_char_in_string, \
    digits_in_string, special_character_in_string, two_strings_are_the_same, validate_email_address


class CreateAccountPageController:
    def __init__(self, root, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.create_account_view = CreateAccountPageView(self.root, self, self.bg_color)
        self.create_account_model = CreateAccountPageModel()

    '''
    Check all conditions combined and if all is correct create account and sent confirm email, then going back to 
    login page 
    '''
    def create_account(self, login_input: str, password_input: str, repeat_password_input: str, email_input: str,
                       notifications: bool):
        if self.login_validate(login_input) and \
                self.password_validate(password_input) and \
                self.repeat_password_validate(password_input, repeat_password_input) and \
                self.email_validate(email_input):

            self.create_account_model.insert_user_to_database(login_input, password_input, email_input, notifications,
                                                              self.create_account_model.get_today_date())
            self.create_account_model.account_created_successfully_email(email_input)
            self.create_account_view.destroy_create_account_frame()

            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root, self.bg_color)
            messagebox.showinfo(title="Information", message="Your account has been created, now you can login")

    # Check if login meets requirements
    def login_validate(self, login_input: str) -> bool:
        if not length_of_string_more_equal_than(login_input, 6):
            messagebox.showerror(title='Error', message="Your login is too short.")
            return False
        if not self.create_account_model.check_user_in_database(login_input):
            messagebox.showerror(title='Error', message="This login already exists, try again")
            return False
        return True

    # Check if password meets requirements
    @staticmethod
    def password_validate(password_input: str) -> bool:
        if not length_of_string_more_equal_than(password_input, 8):
            messagebox.showerror(title='Error', message="Your password is too short.")
            return False
        if not lower_char_in_string(password_input):
            messagebox.showerror(title='Error', message="Your password is missing small letter.")
            return False
        if not upper_char_in_string(password_input):
            messagebox.showerror(title='Error', message="Your password is missing large letter.")
            return False
        if not digits_in_string(password_input):
            messagebox.showerror(title='Error', message="Your password is missing digit.")
            return False
        if not special_character_in_string(password_input):
            messagebox.showerror(title='Error', message="Your password is missing special character.")
            return False
        return True

    # Check if passwords are the same
    @staticmethod
    def repeat_password_validate(password_input: str, repeat_password_input: str) -> bool:
        if not two_strings_are_the_same(password_input, repeat_password_input):
            messagebox.showerror(title='Error', message="Passwords are not the same")
            return False
        return True

    # Check if email is valid
    def email_validate(self, email_input: str) -> bool:
        if not self.create_account_model.check_email_in_database(email_input):
            messagebox.showerror(title='Error', message="This email already exists, try logging in")
            return False
        try:
            validate_email_address(email_input)
        except EmailNotValidError as e:
            messagebox.showerror(title='Error', message=str(e))
            return False
        return True

    # Display question if user wants to go back to login page, then takes action based on decision
    def back(self):
        result = messagebox.askquestion(title='Warning', message="Do you want go back to Login page?")
        if result == "yes":
            self.create_account_view.destroy_create_account_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root, self.bg_color)
        elif result == "no":
            pass
