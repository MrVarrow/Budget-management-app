import mysql.connector
import pandas as pd
import re


class SavingsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def save_goal_to_database(self, user_data, goal_name, goal_amount, goal_date, progress, automatic_deposit):
        insert_query = 'INSERT INTO savingsgoals (username, GoalName, GoalAmount, GoalDate, Progress,' \
                       ' AutomaticDeposit) VALUES (%s, %s, %s, %s, %s, %s)'
        values_to_insert = (user_data[0], goal_name, goal_amount, goal_date, progress, automatic_deposit)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    def delete_goal_from_database(self, user_data, goal_name):
        self.cursor.execute('DELETE FROM savingsgoals WHERE GoalName = %s AND username = %s', (goal_name, user_data[0]))
        self.connection.commit()

    def get_info_about_goal(self, user_data, goal_name):
        goal_info = []
        self.cursor.execute('SELECT * FROM savingsgoals WHERE username = %s AND GoalName = %s', (user_data[0], goal_name))
        row = self.cursor.fetchone()
        if row is not None:
            goal_info = list(row)
        return goal_info

    def goal_amount_validation(self, goal_amount):
        if not re.search(r'^(?!0$)[1-9]\d{0,9}$', goal_amount):
            return False
        return True

    def goal_name_validation(self, goal_name):
        if not re.search(r'^[a-zA-Z][a-zA-Z\s]{0,29}$', goal_name):
            return False
        return True

    def investments_calculator(self, entry_payment, future_payments, frequency_of_payments, investing_time, rate_of_return):
        ...

    def bank_deposit_calculator(self, amount, bank_deposit_time, interest_rate, capitalization_type):
        ...



