import mysql.connector
from SendEmails import send_email_with_code
import random


class AccountPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        self.status_for_user = ''

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

    # Send e-mail with code
    def resend_email_with_code(self, user_email, code):
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

    def user_email_get(self, user_data):
        username = user_data[0]
        self.cursor.execute("SELECT email FROM `user` WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        return row[0]

    def user_password_get(self, user_data):
        username = user_data[0]
        self.cursor.execute("SELECT password FROM `user` WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        return row[0]


    def password_update(self):
        ...
