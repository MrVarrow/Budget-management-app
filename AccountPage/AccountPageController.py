from AccountPage.AccountPageModel import AccountPageModel
from AccountPage.AccountPageView import AccountPageView
from tkinter import messagebox


class AccountPageController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.account_page_view = AccountPageView(self.root, self)
        self.account_page_model = AccountPageModel()
        self.code = ""

    # Account page buttons methods
    def change_password(self):
        ...

    def verify_email(self):
        self.account_page_view.verify_email_window(self.user_data[1])
        self.code = self.account_page_model.generate_code()
        self.account_page_model.resend_email_with_code(self.user_data[1], self.code)

    def send_email(self):
        # resend email with code
        messagebox.showinfo(title="Information", message="E-mail has been sent")

    def submit_code(self, code_entry, code):
        if code_entry == code:
            messagebox.showinfo(title="Information", message="Your account has been successfully verificated")
            # destroy window e-mail
        else:
            messagebox.showinfo(title="Information", message="Wrong code, try again")

    def change_email(self):
        ...

    def change_email_notifications(self):
        ...

    def delete_account(self):
        result = messagebox.askquestion(title='Warning',
                                                message="Do you want to DELETE YOUR ACCOUNT? This action is PERNAMENT.")
        if result == "yes":
            self.account_page_view.account_frame_destroy()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
            ...  # delete acc from database(later)
            messagebox.showinfo(title="Information", message="Your account has been deleted")
        elif result == "no":
            pass

    def clear_all_data(self):
        result = messagebox.askquestion(title='Warning',
                                                message="Do you want to CLEAR ALL DATA? This action is PERNAMENT.")
        if result == "yes":
            ...  # clear all data of user from database but not acc(later)
            messagebox.showinfo(title="Information", message="All of your data has been cleared.")
        elif result == "no":
            pass

    # Verify e-mail window buttons methods

    # Check if code is valid
    def submit_verification_code(self, user_entry_code):
        if self.account_page_model.check_code(user_entry_code, self.code):
            messagebox.showinfo(title="Information", message="Entered code is wrong, double check and try again.")
        else:
            # Add info that user verified e-mail to database
            messagebox.showinfo(title="Information", message="Your e-mail is now verified.")

    # Resend e-mail with code
    def resend_email(self):
        self.account_page_model.resend_email_with_code(self.user_data[1], self.account_page_model.generate_code())