import SendEmails
import mysql.connector
import re
from email_validator import validate_email


class CreateAccountPageModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Check if user login is longer than 6 chars
    def check_login_length(self, login_input):
        if not len(login_input) >= 6:
            return False
        return True

    # Check if user is already in database
    def check_user_in_database(self, login_input):
        self.cursor.execute(
            "SELECT username, COUNT(*) FROM `user` WHERE username = %s",
            (login_input,))
        user_data = self.cursor.fetchone()
        row_count = user_data[1]
        if not row_count == 0:
            return False
        return True

    # Check if user password is at least 8 chars
    def check_password_length(self, password_input):
        if not len(password_input) >= 8:
            return False
        return True

    # Check if user password contains small char
    def check_password_for_small_char(self, password_input):
        if not re.search("[a-z]", password_input):
            return False
        return True

    # Check if user password contains upper char
    def check_password_for_upper_char(self, password_input):
        if not re.search("[A-Z]", password_input):
            return False
        return True

    # Check if user password contains digit
    def check_password_for_numbers(self, password_input):
        if not re.search("[0-9]", password_input):
            return False
        return True

    # Check if user password contains special char
    def check_password_for_special_char(self, password_input):
        if not re.search(r"\W", password_input):
            return False
        return True

    # Check if both passwords are the same
    def check_if_passwords_are_the_same(self, password_input, repeat_password_input):
        if not password_input == repeat_password_input:
            return False
        return True

    # Check if user e-mail is already in database
    def check_email_in_database(self, email_input):
        self.cursor.execute(
            "SELECT email, COUNT(*) FROM `user` WHERE email = %s",
            (email_input,))
        row = self.cursor.fetchone()
        row_count = row[1]
        if not row_count == 0:
            return False
        return True

    # Check if email is valid
    def check_if_email_is_valid(self, email_input):
        v = validate_email(email_input)
        email = v.normalized  # Try to delete variable

    # Inserting user to database "user"
    def insert_user_to_database(self, login_input, password_input, email_input, notifications):
        insert_query = 'INSERT INTO `user` (username, email, password, EmailNotifications) VALUES (%s, %s, %s, %s)'
        values_to_insert = (login_input, email_input, password_input,
                            '1' if notifications else '0')
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Sending e-mail to user
    def account_created_successfully_email(self, email_input):
        SendEmails.send_confirm_email(email_input)
