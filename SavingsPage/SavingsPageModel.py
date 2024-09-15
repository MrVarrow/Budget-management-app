import mysql.connector
import pandas as pd
import re
from datetime import datetime


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

    def goal_date_validation(self, goal_date):
        ...

    def get_user_goals(self, user_data):
        self.cursor.execute('SELECT GoalName FROM savingsgoals WHERE username = %s', (user_data[0],))
        rows = self.cursor.fetchall()
        goals = list(rows)
        return goals

    def update_progress_in_database(self, user_data, goal_name, progress):
        self.cursor.execute('UPDATE savingsgoals SET Progress = %s WHERE username = %s AND GoalName = %s',
                            (progress, user_data[0], goal_name))
        self.connection.commit()

    def update_automatic_deposit_in_database(self, user_data, goal_name, automatic_deposit):
        self.cursor.execute('UPDATE savingsgoals SET AutomaticDeposit = %s WHERE username = %s AND GoalName = %s',
                            (automatic_deposit, user_data[0], goal_name))

    def calculate_time_left_for_goal(self, goal_date):
        today = datetime.now()
        today = datetime.date(today)
        time_left = goal_date - today

        if time_left.total_seconds() < 0:
            return "Expired"

        return time_left.days

    def calculate_percent_of_goal_accomplished(self, goal_amount, progress):
        percent = 0
        if progress == 0:
            return int(percent)
        else:
            percent = (progress / goal_amount) * 100
            return int(percent)

    def investments_calculator(self, entry_payment, future_payments, frequency_of_payments, investing_time, rate_of_return):
        ...

    def bank_deposit_calculator(self, amount, bank_deposit_time, interest_rate, capitalization_type):
        ...



