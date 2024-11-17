import mysql.connector
import pandas as pd
import re


class StatisticsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Converts user time_period input to list of month
    def user_input_to_date(self, time_period):
        ...


