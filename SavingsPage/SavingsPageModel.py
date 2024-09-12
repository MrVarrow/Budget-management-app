import mysql.connector
import pandas as pd
import re


class SavingsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def save_goal_to_database(self, goal_name, goal_amount, goal_date):
        ...

    def delete_goal_from_database(self, goal_name):
        ...

    def get_info_about_goal(self, user_data, goal_name):
        ...

    def investments_calculator(self, entry_payment, future_payments, frequency_of_payments, investing_time, rate_of_return):
        ...

    def bank_deposit_calculator(self, amount, bank_deposit_time, interest_rate, capitalization_type):
        ...



