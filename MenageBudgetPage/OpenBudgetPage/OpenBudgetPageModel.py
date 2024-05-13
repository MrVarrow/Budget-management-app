import mysql.connector
import pandas as pd


class OpenBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def income_from_database(self, user_data):
        ...

    def income_df_creation(self):
        ...

    def expenses_from_database(self, user_data):
        ...

    def expenses_df_creation(self):
        ...

