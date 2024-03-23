import mysql.connector


class RateAppWindowsModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def check_if_has_already_rated_app(self, user_data):
        ...
        # Check in database

