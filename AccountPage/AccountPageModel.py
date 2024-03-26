import mysql.connector
from SendEmails import send_email_with_code
import random

class AccountPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Send e-mail with code
    def resend_email_with_code(self, user_email, code):
        send_email_with_code(user_email, code)

    # Generate code to verify e-mail
    def generate_code(self):
        code = ""
        for digit in range(0, 6):
            digit = random.randint(0, 9)
            code += str(digit)
        return code

    # Check if code is valid
    def check_code(self, user_entry_code, code):
        if not user_entry_code == code:
            return True
        return False

    # Add user to database of users with verified e-mails
    def add_verify_user_to_db(self):
        ...

