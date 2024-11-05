import mysql.connector
import pandas as pd
import re
from datetime import datetime
import matplotlib.pyplot as plt


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
        self.cursor.execute('SELECT * FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        row = self.cursor.fetchone()
        if row is not None:
            goal_info = list(row)
        return goal_info

    def insert_automatic_deposit_to_constants(self, user_data, goal_name, automatic_deposit):
        self.cursor.execute('INSERT INTO consttransactions (Username, Type, Category, Amount) VALUES (%s, %s, %s, %s)',
                            (user_data[0], 'Expense', f'Savings: {goal_name}', automatic_deposit))
        self.connection.commit()
        self.cursor.reset()

    def update_automatic_deposit_to_constants(self, automatic_deposit, goal_name, user_data):
        update_query = 'UPDATE consttransactions SET Amount = %s WHERE Username = %s AND Category = %s'
        values_to_insert = (automatic_deposit, user_data[0], f'Savings: {goal_name}')
        print(
            f"Updating Amount to {int(automatic_deposit)} for Username: {user_data[0]} and Category: Savings{goal_name}")
        try:
            self.cursor.execute(update_query, values_to_insert)
            self.connection.commit()
            print(f"Updated {self.cursor.rowcount} row(s).")
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_if_deposit_exists(self, user_data, goal_name):
        self.cursor.execute('SELECT Category FROM consttransactions WHERE Category = %s AND Username = %s',
                            (f'Savings: {goal_name}', user_data[0]))
        row = self.cursor.fetchone()
        self.cursor.reset()
        if row is None:
            return False
        return True

    def goal_amount_validation(self, goal_amount):
        if not re.search(r'^(?!0$)[1-9]\d{0,9}$', goal_amount):
            return False
        return True

    def goal_name_validation(self, goal_name):
        if not re.search(r'^[a-zA-Z][a-zA-Z\s]{0,29}$', goal_name):
            return False
        return True

    def goal_amount_deposit_validation(self, deposit_amount, goal_amount, progress):
        if int(deposit_amount) > int(goal_amount) - int(progress):
            return False
        return True

    def goal_amount_withdraw_validation(self, withdraw_amount, progress):
        if int(withdraw_amount) > int(progress):
            return False
        return True

    def goal_date_validation(self, goal_date):
        today = datetime.now().date()
        if goal_date < today:
            return False
        return True

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
        self.connection.commit()
        self.cursor.reset()

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
            return round(float(percent), 2)

    def get_progress_from_database(self, user_data, goal_name):
        self.cursor.execute('SELECT Progress FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        rows = self.cursor.fetchone()
        self.cursor.reset()
        return rows[0]

    def get_goal_amount_from_database(self, user_data, goal_name):
        self.cursor.execute('SELECT GoalAmount FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        rows = self.cursor.fetchone()
        self.cursor.reset()
        return rows[0]

    def deposit_to_progress(self, old_progress, deposit_amount):
        new_progress = old_progress + deposit_amount
        return new_progress  # check if its larger than 10 digits (cant be)

    def withdraw_from_progress(self, old_progress, withdraw_amount):
        new_progress = old_progress - withdraw_amount
        return new_progress  # check if its negative (cant be)

    def investments_calculator(self, entry_payment, future_payments, frequency_of_payments, investing_time,
                               rate_of_return) -> float:

        entry_payment = float(entry_payment)
        future_payments = float(future_payments)
        frequency_of_payments = int(frequency_of_payments)
        investing_time = int(investing_time)
        rate_of_return = float(rate_of_return)

        future_value_of_entry = entry_payment * pow((1 + rate_of_return / frequency_of_payments),
                                                    frequency_of_payments * investing_time)
        future_value_of_payments = future_payments * (pow((1 + rate_of_return / frequency_of_payments),
                                                          frequency_of_payments *
                                                          investing_time) - 1) / (rate_of_return /
                                                                                  frequency_of_payments)

        total_future_value = future_value_of_entry + future_value_of_payments

        return round(total_future_value, 2)

    def bank_deposit_calculator(self, amount, bank_deposit_time, interest_rate, capitalization_type):
        amount = float(amount)  # Principal amount
        bank_deposit_time = int(bank_deposit_time)  # Duration in years
        interest_rate = float(interest_rate)  # Annual interest rate
        capitalization_type = int(capitalization_type)  # Compounding

        future_value = amount * (1 + interest_rate / capitalization_type) ** (capitalization_type * bank_deposit_time)

        return round(future_value, 2)

    def create_plot_dataframe_investments(self, profit_df: pd.DataFrame):
        fig, ax = plt.subplots()
        profit_df.plot(x='year', y='amount', kind='line', ax=ax)
        plt.title('Value of your investments')
        plt.xlabel('Year')
        plt.ylabel('Investments Value')
        return fig

    def create_plot_dataframe_bank_deposit(self, profit_df):
        fig, ax = plt.subplots()
        profit_df.plot(x='year', y='amount', kind='line', ax=ax)
        plt.title('Value of your bank deposit')
        plt.xlabel('Year')
        plt.ylabel('Bank deposit Value')
        return fig

    def create_profit_dataframe(self, years: list, amounts: list) -> pd.DataFrame:
        data = {
            "year": years,
            "amount": amounts
        }
        profit_df = pd.DataFrame(data)
        return profit_df
