import SendEmails
import mysql.connector


class CreateAccountPageModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def email_validate(self):
        ...

    def check_login_requirements(self):
        ...

    def check_password_requirements(self):
        ...

    def check_if_passwords_are_the_same(self):
        ...

    # Probably in controller in future
    def account_created_successfully(self):
        ...
