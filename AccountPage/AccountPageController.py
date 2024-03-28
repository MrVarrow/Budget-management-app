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
        self.account_page_view.change_password_window()

    def verify_email(self):
        self.account_page_view.verify_email_window(self.user_data[1])
        self.code = self.account_page_model.generate_code()
        self.account_page_model.resend_email_with_code(self.user_data[1], self.code)

    def send_email(self):
        # resend email with code
        messagebox.showinfo(title="Information", message="E-mail has been sent")

    def change_email(self):
        ...

    def change_email_notifications(self):
        status = self.account_page_model.email_notifications_status(self.user_data)
        result = messagebox.askquestion(title='Warning',
                                        message="Do you want to change your emails notification settings\n"
                                                "status: {}".format(self.account_page_model.status_for_user))
        if result == 'yes':
            self.account_page_model.email_notifications_status_change(self.user_data, status)
        elif result == "no":
            pass

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
            self.account_page_model.add_verify_user_to_db(self.user_data, True)
            self.account_page_view.verify_email_root_destroy()
            messagebox.showinfo(title="Information", message="Your e-mail is now verified.")

    # Resend e-mail with code
    def resend_email(self):
        self.account_page_model.resend_email_with_code(self.user_data[1], self.account_page_model.generate_code())

    # Change e-mail window buttons methods

    # Change password window buttons methods

    # Not sure about this rn but works
    def submit_password(self, password_input, repeat_password_input):
        from CreateAccountPage.CreateAccountController import CreateAccountPageController
        self.create_account_page_controller = CreateAccountPageController.__call__(CreateAccountPageController(self.root), self.user_data, password_input, repeat_password_input)
        if self.create_account_page_controller:
            print("to database")
        print("")
