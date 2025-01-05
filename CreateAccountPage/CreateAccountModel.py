import SendEmails
import mysql.connector
from datetime import datetime


class CreateAccountPageModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Check if user is already in database
    def check_user_in_database(self, login_input: str) -> bool:
        self.cursor.execute(
            "SELECT username, COUNT(*) FROM `user` WHERE username = %s",
            (login_input,))
        user_data = self.cursor.fetchone()
        row_count = user_data[1]
        if not row_count == 0:
            return False
        return True

    # Check if user e-mail is already in database
    def check_email_in_database(self, email_input: str) -> bool:
        self.cursor.execute(
            "SELECT email, COUNT(*) FROM `user` WHERE email = %s",
            (email_input,))
        row = self.cursor.fetchone()
        row_count = row[1]
        if not row_count == 0:
            return False
        return True

    # Inserting user to database "user"
    def insert_user_to_database(self, login_input: str, password_input: str, email_input: str, notifications: bool,
                                today_date: datetime):
        insert_query = '''
                       INSERT INTO `user` (username, email, password, EmailNotifications, rating, emailverification,
                       lastseen)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                       '''
        values_to_insert = (login_input, email_input, password_input,
                            '1' if notifications else '0', '0', False, today_date)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Sending e-mail to user
    @staticmethod
    def account_created_successfully_email(email_input: str):
        SendEmails.send_confirm_email(email_input)

    @staticmethod
    def get_today_date():
        today = datetime.now()
        today = datetime.date(today)
        return today
