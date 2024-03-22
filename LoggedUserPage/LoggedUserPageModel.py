import SendEmails
import mysql.connector


# I think that file is useless right now. I don't know if this will change in future
class LoggedUserPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

