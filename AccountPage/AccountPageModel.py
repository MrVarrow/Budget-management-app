import mysql.connector
from SendEmails import send_email_with_code
import random


class AccountPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        self.status_for_user = ''

    def email_verification_status(self, user_data: tuple) -> bool:
        self.cursor.execute("SELECT emailverification FROM `user` WHERE username = %s", (user_data[0],))
        row = self.cursor.fetchone()

        return row[0]

    '''
    E-MAIL NOTIFICATIONS METHODS
    '''

    # Get email notification status from database
    def email_notifications_status(self, user_data: tuple) -> bool:
        self.cursor.execute("SELECT EmailNotifications FROM `user` WHERE username = %s", (user_data[0],))
        row = self.cursor.fetchone()
        if row[0] == 0:
            self.status_for_user = 'disagree'
        elif row[0] == 1:
            self.status_for_user = 'agree'
        return row[0]

    # Update status of email notification status
    def email_notifications_status_change(self, user_data: tuple, status: bool):
        if status == 0:
            status = 1
        elif status == 1:
            status = 0
        self.cursor.execute('UPDATE budgetappdatabase.user SET EmailNotifications = %s WHERE username = %s',
                            (status, user_data[0]))
        self.connection.commit()

    '''
    E-MAIL VERIFICATION METHODS
    '''

    # Send e-mail with code
    @staticmethod
    def send_email_with_code(user_email: str, code: str):
        send_email_with_code(user_email, code)

    # Generate code to verify e-mail
    @staticmethod
    def generate_code() -> str:
        code = ""
        for digit in range(0, 6):
            digit = random.randint(0, 9)
            code += str(digit)
            print(code)
        return code

    # Update user verify status in database
    def add_verify_user_to_db(self, user_data: tuple, email_verification_status: bool):
        self.cursor.execute('UPDATE budgetappdatabase.user SET emailverification = %s WHERE username = %s',
                            (email_verification_status, user_data[0]))
        self.connection.commit()

    '''
    E-MAIL CHANGE METHODS
    '''

    # Check if new e-mail is already in database
    def check_new_email_in_database(self, new_email_entry: str) -> bool:
        self.cursor.execute(
            "SELECT email, COUNT(*) FROM `user` WHERE email = %s",
            (new_email_entry,))
        row = self.cursor.fetchone()
        row_count = row[1]
        if not row_count == 0:
            return False
        return True

    # Update user email to new one
    def update_user_email(self, user_data: tuple, new_email_entry: str):
        self.cursor.execute('UPDATE budgetappdatabase.user SET email = %s WHERE username = %s',
                            (new_email_entry, user_data[0]))
        self.connection.commit()

    '''
    PASSWORD CHANGE METHODS
    '''

    # Update user password to new one
    def update_user_new_password(self, user_data: tuple, new_password_entry: str):
        self.cursor.execute('UPDATE budgetappdatabase.user SET password = %s WHERE username = %s',
                            (new_password_entry, user_data[0]))
        self.connection.commit()

    '''
    Clear Data methods
    '''

    def clear_data_from_db(self, user_data: tuple):
        self.cursor.execute('DELETE FROM budgetappdatabase.shoppinglists WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.shoppinglistitems WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.savingsgoals WHERE username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.receipts WHERE UserName = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.receiptitems WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.monthbudget WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.budgettransactions WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.constbudget WHERE Username = %s', (user_data[0],))
        self.cursor.execute('DELETE FROM budgetappdatabase.consttransactions WHERE Username = %s', (user_data[0],))
        self.connection.commit()

    '''
    Delete account methods
    '''

    def delete_user_from_db(self, user_data: tuple):
        self.cursor.execute('DELETE FROM user WHERE username = %s', (user_data[0],))
        self.connection.commit()
