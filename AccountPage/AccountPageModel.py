import mysql.connector
from SendEmails import send_email_with_code
import random
from CreateAccountPage.CreateAccountModel import CreateAccountPageModel


class AccountPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        self.status_for_user = ''
        self.create_account_model = CreateAccountPageModel()

    # E-MAIL NOTIFICATIONS METHODS
    # Get email notification status from database
    def email_notifications_status(self, user_data):
        username = user_data[0]
        self.cursor.execute("SELECT EmailNotifications FROM `user` WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        if row[0] == 0:
            self.status_for_user = 'disagree'
        elif row[0] == 1:
            self.status_for_user = 'agree'
        return row[0]

    # Update status of email notification status
    def email_notifications_status_change(self, user_data, status):
        if status == 0:
            status = 1
        elif status == 1:
            status = 0
        self.cursor.execute('UPDATE budgetappdatabase.user SET EmailNotifications = %s WHERE username = %s',
                            (status, user_data[0]))
        self.connection.commit()

    # E-MAIL VERIFICATION METHODS
    # Send e-mail with code
    def send_email_with_code(self, user_email, code):
        send_email_with_code(user_email, code)

    # Generate code to verify e-mail
    def generate_code(self):
        code = ""
        for digit in range(0, 6):
            digit = random.randint(0, 9)
            code += str(digit)
            print(code)
        return code

    # Check if code is valid
    def check_code(self, user_entry_code, code):
        if not user_entry_code == code:
            return True
        return False

    # Update user verify status in database
    def add_verify_user_to_db(self, user_data, email_verification_status):
        self.cursor.execute('UPDATE budgetappdatabase.user SET emailverification = %s WHERE username = %s',
                            (email_verification_status, user_data[0]))
        self.connection.commit()

    # E-MAIL CHANGE METHODS
    # E-mail validation
    def new_email_validate(self, new_email_entry):
        result = self.create_account_model.check_if_email_is_valid(new_email_entry)
        return result

    # Check if new e-mail is already in database
    def check_new_email_in_database(self, new_email_entry):
        result = self.create_account_model.check_email_in_database(new_email_entry)
        return result

    # Check if entered old e-mail is correct
    def check_if_old_email_is_correct(self, old_email_entry, user_data):
        if not old_email_entry == user_data[1]:
            return False
        return True

    # Update user email to new one
    def update_user_email(self, user_data, new_email_entry):
        self.cursor.execute('UPDATE budgetappdatabase.user SET email = %s WHERE username = %s',
                            (new_email_entry, user_data[0]))
        self.connection.commit()

    # Check if both entered e-mails are the same
    def check_if_emails_are_the_same(self, new_email_entry, new_email_reentry):
        if not new_email_entry == new_email_reentry:
            return False
        return True

    # Check if old e-mail is the same as new e-mail
    def check_if_old_is_new_email(self, new_email_entry, user_data):
        if not new_email_entry != user_data[1]:
            return False
        return True

    # PASSWORD CHANGE METHODS
    # Check if user password is at least 8 chars
    def check_new_password_length(self, new_password_entry):
        result = self.create_account_model.check_password_length(new_password_entry)
        return result

    # Check if user password contains small char
    def check_new_password_for_small_char(self, new_password_entry):
        result = self.create_account_model.check_password_for_small_char(new_password_entry)
        return result

    # Check if user password contains upper char
    def check_new_password_for_upper_char(self, new_password_entry):
        result = self.create_account_model.check_password_for_upper_char(new_password_entry)
        return result

    # Check if user password contains digit
    def check_new_password_for_numbers(self, new_password_entry):
        result = self.create_account_model.check_password_for_numbers(new_password_entry)
        return result

    # Check if user password contains special char
    def check_new_password_for_special_char(self, new_password_entry):
        result = self.create_account_model.check_password_for_special_char(new_password_entry)
        return result

    # Check if both passwords are the same
    def check_if_new_passwords_are_the_same(self, new_password_entry, new_password_reentry):
        result = self.create_account_model.check_if_passwords_are_the_same(new_password_entry, new_password_reentry)
        return result

    # Check if entered old password is correct
    def check_if_old_password_is_correct(self, old_password_entry, user_data):
        if not old_password_entry == user_data[2]:
            return False
        return True

    # Update user password to new one
    def update_user_new_password(self, user_data, new_password_entry):
        self.cursor.execute('UPDATE budgetappdatabase.user SET password = %s WHERE username = %s',
                            (new_password_entry, user_data[0]))
        self.connection.commit()

    # Check if old password is the same as new password
    def check_if_old_is_new_password(self, new_password_entry, user_data):
        if not new_password_entry != user_data[2]:
            return False
        return True
