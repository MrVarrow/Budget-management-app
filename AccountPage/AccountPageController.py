from AccountPage.AccountPageModel import AccountPageModel
from AccountPage.AccountPageView import AccountPageView
from tkinter import messagebox
from email_validator import EmailNotValidError


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
        # TO DO: if email is already verified return and display message
        self.account_page_view.verify_email_window(self.user_data[1])
        self.code = self.account_page_model.generate_code()
        self.send_email()

    def change_email(self):
        self.account_page_view.change_email_window()

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
                                        message="Do you want to DELETE YOUR ACCOUNT? This action is PERMANENT.")
        if result == "yes":
            self.account_page_view.account_frame_destroy()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root)
            ...  # delete acc from database(later) and clear all data
            messagebox.showinfo(title="Information", message="Your account has been deleted")
        elif result == "no":
            pass

    def clear_all_data(self):
        result = messagebox.askquestion(title='Warning',
                                        message="Do you want to CLEAR ALL DATA? This action is PERMANENT.")
        if result == "yes":
            ...  # clear all data of user from database but not acc(later)
            messagebox.showinfo(title="Information", message="All of your data has been cleared.")
        elif result == "no":
            pass

    def back_from_acc_page(self):
        ...

    # Verify e-mail window buttons methods

    # Check all conditions then change status
    def submit_verification_code(self, user_entry_code):
        if self.account_page_model.check_code(user_entry_code, self.code):
            messagebox.showinfo(title="Information", message="Entered code is wrong, double check and try again.")
        else:
            self.account_page_model.add_verify_user_to_db(self.user_data, True)
            self.account_page_view.verify_email_root_destroy()
            messagebox.showinfo(title="Information", message="Your e-mail is now verified.")

    # Sends e-mail with code
    def send_email(self):
        self.account_page_model.send_email_with_code(self.user_data[1], self.code)
        messagebox.showinfo(title="Information", message="E-mail has been sent")

    # Change password window buttons methods
    def submit_password(self, old_password_entry, new_password_entry, new_password_reentry):
        if self.old_password_check(old_password_entry) and \
                self.new_password_validate(new_password_entry) and \
                self.new_is_old_password_check(new_password_entry) and \
                self.repeat_new_password_validate(new_password_entry, new_password_reentry):
            self.account_page_model.update_user_new_password(self.user_data, new_password_entry)
            self.account_page_view.change_password_window_destroy()
            messagebox.showinfo(title="Information", message="Your password has been successfully changed.")
        '''
        from CreateAccountPage.CreateAccountController import CreateAccountPageController
        self.create_account_page_controller = CreateAccountPageController.__call__(CreateAccountPageController(self.root), self.user_data, password_input, repeat_password_input)
        if self.create_account_page_controller:
            print("to database")
        print("")
        '''

    # Check and display potential errors to user for changing password
    def new_password_validate(self, new_password_entry):
        if not self.account_page_model.check_new_password_length(new_password_entry):
            messagebox.showerror(title='Error', message="Your password is too short.")
            return False
        if not self.account_page_model.check_new_password_for_small_char(new_password_entry):
            messagebox.showerror(title='Error', message="Your password is missing small letter.")
            return False
        if not self.account_page_model.check_new_password_for_upper_char(new_password_entry):
            messagebox.showerror(title='Error', message="Your password is missing large letter.")
            return False
        if not self.account_page_model.check_new_password_for_numbers(new_password_entry):
            messagebox.showerror(title='Error', message="Your password is missing digit.")
            return False
        if not self.account_page_model.check_new_password_for_special_char(new_password_entry):
            messagebox.showerror(title='Error', message="Your password is missing special character.")
            return False
        return True

    def repeat_new_password_validate(self, new_password_entry, new_password_reentry):
        if not self.account_page_model.check_if_new_passwords_are_the_same(new_password_entry, new_password_reentry):
            messagebox.showerror(title='Error', message="New Passwords are not the same")
            return False
        return True

    def old_password_check(self, old_password_entry):
        if not self.account_page_model.check_if_old_password_is_correct(old_password_entry, self.user_data):
            messagebox.showerror(title='Error', message="Old password is not correct")
            return False
        return True

    def new_is_old_password_check(self, new_password_entry):
        if not self.account_page_model.check_if_old_is_new_password(new_password_entry, self.user_data):
            messagebox.showerror(title='Error', message="Old password can't be your new password.")
            return False
        return True

    # Change e-mail window button methods
    def submit_email(self, old_email_entry, new_email_entry, new_email_reentry):
        if self.old_email_check(old_email_entry) and \
                self.new_email_validation(new_email_entry) and \
                self.new_is_old_email_check(new_email_entry) and \
                self.repeat_email_validate(new_email_entry, new_email_reentry):
            self.account_page_model.update_user_email(self.user_data, new_email_entry)
            # Change verification e-mail status to False
            self.account_page_model.add_verify_user_to_db(self.user_data, True)
            self.account_page_view.change_email_window_destroy()
            messagebox.showinfo(title="Information", message="Your e-mail has been successfully changed.")

    # Check and display potential errors to user for changing e-mail
    def new_email_validation(self, new_email_entry):
        if not self.account_page_model.check_new_email_in_database(new_email_entry):
            messagebox.showerror(title='Error', message="This e-mail is already registered, try again")
            return False
        try:
            self.account_page_model.new_email_validate(new_email_entry)
        except EmailNotValidError as e:
            messagebox.showerror(title='Error', message=str(e))
            return False
        return True

    def old_email_check(self, old_email_entry):
        if not self.account_page_model.check_if_old_email_is_correct(old_email_entry, self.user_data):
            messagebox.showerror(title='Error', message="Your old email is not correct.")
            return False
        return True

    def repeat_email_validate(self, new_email_entry, new_email_reentry):
        if not self.account_page_model.check_if_emails_are_the_same(new_email_entry, new_email_reentry):
            messagebox.showerror(title='Error', message="New e-mails are not the same.")
            return False
        return True

    def new_is_old_email_check(self, new_email_entry):
        if not self.account_page_model.check_if_old_is_new_email(new_email_entry, self.user_data):
            messagebox.showerror(title='Error', message="Old e-mail can't be your new e-mail.")
            return False
        return True
