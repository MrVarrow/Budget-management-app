import mysql.connector
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


class SavingsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    '''
    Database operations
    '''

    # Insert goal to database
    def save_goal_to_database(self, user_data: tuple, goal_name: str, goal_amount: str, goal_date, progress: int,
                              automatic_deposit: int):
        insert_query = 'INSERT INTO savingsgoals (username, GoalName, GoalAmount, GoalDate, Progress,' \
                       ' AutomaticDeposit) VALUES (%s, %s, %s, %s, %s, %s)'
        values_to_insert = (user_data[0], goal_name, goal_amount, goal_date, progress, automatic_deposit)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Delete goal with given name from database
    def delete_goal_from_database(self, user_data: tuple, goal_name: str):
        self.cursor.execute('DELETE FROM savingsgoals WHERE GoalName = %s AND username = %s', (goal_name, user_data[0]))
        self.connection.commit()

    # Get info about goal with given name from database
    def get_info_about_goal(self, user_data: tuple, goal_name: str) -> list:
        goal_info = []
        self.cursor.execute('SELECT * FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        row = self.cursor.fetchone()
        if row is not None:
            goal_info = list(row)
        return goal_info

    # Insert automatic deposit to constants transactions
    def insert_automatic_deposit_to_constants(self, user_data: tuple, goal_name: str, automatic_deposit: str):
        self.cursor.execute('INSERT INTO consttransactions (Username, Type, Category, Amount) VALUES (%s, %s, %s, %s)',
                            (user_data[0], 'Expense', f'Savings: {goal_name}', automatic_deposit))
        self.connection.commit()
        self.cursor.reset()

    # Update automatic deposit in constants
    def update_automatic_deposit_to_constants(self, automatic_deposit: int, goal_name: str, user_data: tuple):
        update_query = 'UPDATE consttransactions SET Amount = %s WHERE Username = %s AND Category = %s'
        values_to_insert = (automatic_deposit, user_data[0], f'Savings: {goal_name}')
        self.cursor.execute(update_query, values_to_insert)
        self.connection.commit()

    # Check if constants transactions budget exists
    def check_if_deposit_exists(self, user_data: tuple, goal_name: str) -> bool:
        self.cursor.execute('SELECT Category FROM consttransactions WHERE Category = %s AND Username = %s',
                            (f'Savings: {goal_name}', user_data[0]))
        row = self.cursor.fetchone()
        self.cursor.reset()
        if row is None:
            return False
        return True

    # Get list of user goal names
    def get_user_goals(self, user_data: tuple) -> list:
        self.cursor.execute('SELECT GoalName FROM savingsgoals WHERE username = %s', (user_data[0],))
        rows = self.cursor.fetchall()
        goals = list(rows)
        return goals

    # Updates progress value in database
    def update_progress_in_database(self, user_data: tuple, goal_name: str, progress: float):
        self.cursor.execute('UPDATE savingsgoals SET Progress = %s WHERE username = %s AND GoalName = %s',
                            (progress, user_data[0], goal_name))
        self.connection.commit()

    # Updates automatic deposit value in database
    def update_automatic_deposit_in_database(self, user_data: tuple, goal_name: str, automatic_deposit: str):
        self.cursor.execute('UPDATE savingsgoals SET AutomaticDeposit = %s WHERE username = %s AND GoalName = %s',
                            (automatic_deposit, user_data[0], goal_name))
        self.connection.commit()
        self.cursor.reset()

    # Gets goal progress with given name from database
    def get_progress_from_database(self, user_data: tuple, goal_name: str) -> float:
        self.cursor.execute('SELECT Progress FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        rows = self.cursor.fetchone()
        self.cursor.reset()
        return rows[0]

    # Gets goal amount with given name from database
    def get_goal_amount_from_database(self, user_data: tuple, goal_name: str) -> float:
        self.cursor.execute('SELECT GoalAmount FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        rows = self.cursor.fetchone()
        self.cursor.reset()
        return rows[0]

    '''
    Calculations
    '''

    # Calculates time left from today to given date
    @staticmethod
    def calculate_time_left_for_goal(goal_date) -> str:
        today = datetime.now()
        today = datetime.date(today)
        time_left = goal_date - today

        if time_left.total_seconds() < 0:
            return "Expired"

        return f"{time_left.days} days"

    # Calculates percent of goal accomplished
    @staticmethod
    def calculate_percent_of_goal_accomplished(goal_amount: str, progress: float) -> float:
        percent = 0
        if not progress == 0:
            percent = (progress / float(goal_amount)) * 100

        return round(float(percent), 2)

    # Calculate sum between 2 integers
    @staticmethod
    def deposit_to_progress(old_progress: float, deposit_amount: int) -> float:
        new_progress = old_progress + deposit_amount
        return new_progress

    # Convert percent(int) to its float substitute
    @staticmethod
    def convert_percent_to_float(percent: float) -> float:
        converted = percent / 100
        return round(converted, 2)

    # Calculate difference between 2 integers
    @staticmethod
    def withdraw_from_progress(old_progress: float, withdraw_amount: int) -> float:
        new_progress = old_progress - withdraw_amount
        return new_progress

    # Calculate value of investments overtime
    @staticmethod
    def investments_calculator(entry_payment: float, future_payments: float, frequency_of_payments: int,
                               investing_time: int, rate_of_return: float) -> tuple:
        list_of_future_values = []
        list_of_years = []
        list_of_money_deposited = []
        money_deposited = entry_payment
        for i in range(investing_time + 1):
            future_value_of_entry = entry_payment * pow((1 + rate_of_return / frequency_of_payments),
                                                        frequency_of_payments * i)
            future_value_of_payments = future_payments * (pow((1 + rate_of_return / frequency_of_payments),
                                                              frequency_of_payments *
                                                              i) - 1) / (rate_of_return / frequency_of_payments)

            total_future_value = future_value_of_entry + future_value_of_payments
            list_of_future_values.append(round(total_future_value, 2))
            list_of_years.append(i)

            list_of_money_deposited.append(money_deposited)
            money_deposited += future_payments * 12

        return list_of_future_values, list_of_years, list_of_money_deposited

    # Calculate value of bank deposit using formula (with capitalization)
    @staticmethod
    def bank_deposit_calculator_capitalization(amount: float, bank_deposit_time: int, interest_rate: float,
                                               capitalization_type: int) -> tuple:
        list_of_future_values = []
        list_of_years = []
        list_of_money_deposited = []
        for i in range(bank_deposit_time + 1):
            future_value = amount * (1 + interest_rate / capitalization_type) ** (capitalization_type * i)
            list_of_future_values.append(round(future_value, 2))
            list_of_years.append(i)
            list_of_money_deposited.append(amount)

        return list_of_future_values, list_of_years, list_of_money_deposited

    # Calculate value of bank deposit using formula (without capitalization)
    @staticmethod
    def bank_deposit_calculator_no_capitalization(amount: float, bank_deposit_time: int, interest_rate: float) -> tuple:

        list_of_future_values = [amount]
        list_of_years = [0, bank_deposit_time]
        list_of_money_deposited = [amount, amount]

        profit = amount * interest_rate * bank_deposit_time
        future_value = amount + profit
        list_of_future_values.append(round(future_value, 2))

        return list_of_future_values, list_of_years, list_of_money_deposited

    '''
    Graph preparation
    '''

    # Create plot for a graph
    def create_plot_dataframe_investments(self, profit_df, deposited_amount_df):
        fig, ax = plt.subplots()
        profit_df.plot(x='year', y='amount', kind='line', ax=ax, label='Investment Value', color='blue', marker='o')

        deposited_amount_df.plot(x='year', y='amount', kind='line', ax=ax, label='Deposited Amount', color='orange',
                                 marker='o')

        # Annotating the profit line
        self.annotate_a_line(ax, profit_df, number=10)

        # Annotating the deposited amount line
        self.annotate_a_line(ax, deposited_amount_df, number=-10)

        plt.title('Value of your money')
        plt.xlabel('Year')
        plt.ylabel('Value')
        return fig

    # Annotates a line in plot for given dataframe
    @staticmethod
    def annotate_a_line(ax, df, number: int):
        for i in range(len(df)):
            ax.annotate(f'{int(df["amount"].iloc[i]):,}',
                        (df['year'].iloc[i], df['amount'].iloc[i]),
                        textcoords="offset points",
                        xytext=(0, number),
                        ha='center',
                        fontsize=8,
                        color='black')

    '''
    Other methods
    '''

    # Create dataframe with : "year", "amount" columns
    @staticmethod
    def create_profit_dataframe(years: list, amounts: list) -> pd.DataFrame:
        data = {
            "year": years,
            "amount": amounts
        }
        profit_df = pd.DataFrame(data)
        return profit_df

    # Get last value from a list
    @staticmethod
    def get_total_investments_value(list_of_future_values: list) -> float:
        return list_of_future_values[-1]
