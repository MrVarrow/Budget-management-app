import mysql.connector
import pyperclip
from SendEmails import send_email_with_link


class MobileAppWindowsModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Copy link to the app to clipboard
    def copy_app_link(self, link):
        pyperclip.copy(link)

    # Sends e-mail with link do download the app to user
    def send_email_with_link(self, link, receiver):
        send_email_with_link(receiver, link)
