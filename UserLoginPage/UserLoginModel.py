import SendEmails
import mysql.connector


class UserLoginModel:
    def __init__(self):
        # Connecting to MySQL local database and setting cursor
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Sending E-mail with password to the user on E-mail assigned to username that user provided
    @staticmethod
    def email_with_password(user_data: tuple):
        receiver = user_data[1]
        password = user_data[2]
        SendEmails.forgot_password_email(receiver, password)

    # Takes entered login from user and looking for them in database, then returning all data stored for that user
    def get_user_data(self, login_input: str) -> tuple:
        username = login_input
        self.cursor.execute("SELECT * FROM `user` WHERE username = %s", (username,))
        user_data = self.cursor.fetchone()
        return user_data
