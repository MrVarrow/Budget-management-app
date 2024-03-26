from AccountPage.AccountPageModel import AccountPageModel
from AccountPage.AccountPageView import AccountPageView
from tkinter import messagebox


class AccountPageController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.account_page_view = AccountPageView(self.root, self)
        self.account_page_model = AccountPageModel()

    def change_password(self):
        ...

    def verify_email(self):
         # Window for e mail verification


          # get from database(later)
         # generate random code with 6 chars
         # Send email with code

        ...

    def resend_email(self):
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
            messagebox.showinfo(title="Information", message="All of your data has been cleared")
        elif result == "no":
            pass
