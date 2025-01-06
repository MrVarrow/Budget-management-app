import mysql.connector
from datetime import datetime
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from typing import Union


class StatisticsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    @staticmethod
    def get_current_month() -> list:
        current_date = datetime.now()
        formatted_month_year = current_date.strftime("%m/%Y")

        return [formatted_month_year]

    @staticmethod
    def get_time_period_in_int(time_period: str) -> int:
        time_period_dict = {"Last Month": 1, "Last 6 Months": 6, "Last Year": 12, "Last 5 Years": 60,
                            "Last 10 Years": 120, "All time": "*"}

        return time_period_dict[time_period]

    @staticmethod
    def get_list_of_months(time_period: int) -> list:
        today = datetime.today()

        months = []

        start_date = today - relativedelta(months=1)

        for i in range(time_period):
            # Calculate the month and year
            month_date = start_date - relativedelta(months=i)
            formatted_month = month_date.strftime("%m/%Y")
            months.append(formatted_month)

        return months

    def get_budget_month_info(self, user_data: tuple, month: str) -> list:

        if month == self.get_current_month()[-1]:
            self.cursor.execute(
                '''
                SELECT * FROM monthbudget 
                WHERE Username = %s 
                AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
                ''',
                (user_data[0], month, month)
            )

            rows = self.cursor.fetchall()
            months_info = [[row[i] for i in [2, 3, 4]] for row in rows]
        else:
            self.cursor.execute(
                '''
                SELECT * FROM monthbudget 
                WHERE Username = %s 
                AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
                AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
                ''',
                (user_data[0], month, month, self.get_current_month()[-1], self.get_current_month()[-1])
            )

            rows = self.cursor.fetchall()
            months_info = [[row[i] for i in [2, 3, 4]] for row in rows]

        return months_info

    @staticmethod
    def add_all_values(months_info: list) -> list:
        combined_values = [sum(values) for values in zip(*months_info)]
        return combined_values

    '''
    General stats
    '''

    def get_categories_for_expenses(self, user_data: tuple) -> list:
        list_of_expenses_categories = []
        self.cursor.execute('SELECT Category FROM budgettransactions WHERE username = %s AND type = %s ',
                            (user_data[0], "Expense"))
        rows_not_const = self.cursor.fetchall()
        for row in rows_not_const:
            list_of_expenses_categories.append(row[0])
        self.cursor.reset()

        self.cursor.execute('SELECT Category FROM consttransactions WHERE username = %s AND type = %s',
                            (user_data[0], "Expense"))
        rows_const = self.cursor.fetchall()
        for row in rows_const:
            list_of_expenses_categories.append(row[0])
        self.cursor.reset()

        list_of_expenses_categories = list(set(list_of_expenses_categories))

        return list_of_expenses_categories

    def get_categories_for_incomes(self, user_data: tuple) -> list:
        list_of_incomes_categories = []
        self.cursor.execute('SELECT Category FROM budgettransactions WHERE username = %s AND type = %s',
                            (user_data[0], "Income"))
        rows_not_const = self.cursor.fetchall()
        for row in rows_not_const:
            list_of_incomes_categories.append(row[0])
        self.cursor.reset()

        self.cursor.execute('SELECT Category FROM consttransactions WHERE username = %s AND type = %s',
                            (user_data[0], "Income"))
        rows_const = self.cursor.fetchall()
        for row in rows_const:
            list_of_incomes_categories.append(row[0])
        self.cursor.reset()

        list_of_incomes_categories = list(set(list_of_incomes_categories))

        return list_of_incomes_categories

    def get_values_from_database(self, user_data: tuple, c_type: str, category: str, month: str) -> list:
        if c_type == "spent":
            type_info = "Expense"
        else:  # elif type == "earned":
            type_info = "Income"
        list_of_values = []
        self.cursor.execute(
            '''
            SELECT Amount FROM budgettransactions 
            WHERE username = %s 
            AND Type = %s 
            AND Category = %s
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
            ''',
            (user_data[0], type_info, category, month, month, self.get_current_month()[-1],
             self.get_current_month()[-1]))
        rows = self.cursor.fetchall()

        if rows is not None:
            for row in rows:
                list_of_values.append(row[0])
        self.cursor.reset()

        if c_type == "spent":
            type_info = "ConstExpense"
        elif c_type == "earned":
            type_info = "ConstIncome"

        self.cursor.execute(
            '''
            SELECT Amount FROM budgettransactions 
            WHERE username = %s 
            AND Type = %s 
            AND Category = %s
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
            ''',
            (user_data[0], type_info, category, month, month, self.get_current_month()[-1],
             self.get_current_month()[-1]))
        rows = self.cursor.fetchall()

        if rows is not None:
            for row in rows:
                list_of_values.append(row[0])

        return list_of_values

    @staticmethod
    def calculate_sum_of_values(values: list) -> float:
        return sum(values)

    '''
    Avg month stats
    '''

    def values_from_db(self, user_data: tuple, month: str) -> list:
        self.cursor.execute(
            '''
            SELECT * FROM monthbudget 
            WHERE Username = %s 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
            ''',
            (user_data[0], month, month, self.get_current_month()[-1], self.get_current_month()[-1])
        )
        rows = self.cursor.fetchall()
        values = [[row[i] for i in [2, 3, 4]] for row in rows]
        return values

    @staticmethod
    def sort_data(values: list) -> tuple:
        incomes_list, expenses_list, free_amount_list = zip(*values)
        return list(incomes_list), list(expenses_list), list(free_amount_list)

    @staticmethod
    def calculate_avg_value(values: list) -> int:
        return sum(values) / len(values) if values else 0

    '''
    Percent stats
    '''

    @staticmethod
    def calculate_percent_value(category_amount_dict: dict, total_amount: float) -> dict:
        category_percentage_dict = {}

        # Calculate percentage for each category
        for category, amount in category_amount_dict.items():
            percentage = ((amount / total_amount) * 100) if total_amount > 0 else 0
            category_percentage_dict[category] = {
                'amount': amount,
                'percentage': round(percentage, 2)  # Round to two decimal places
            }

        return category_percentage_dict

    def get_cat_and_amount(self, user_data: tuple, month: str, type_info: str) -> dict:
        category_amount_dict = {}
        self.cursor.execute(
            '''
            SELECT Category, Amount FROM budgettransactions
            WHERE Username = %s
            AND Type = %s 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
            ''',
            (user_data[0], type_info, month, month, self.get_current_month()[-1],
             self.get_current_month()[-1]))
        rows = self.cursor.fetchall()
        for row in rows:
            category = row[0]
            amount = row[1]

            if category in category_amount_dict:
                category_amount_dict[category] += amount
            else:
                category_amount_dict[category] = amount

        return category_amount_dict

    @staticmethod
    def combine_dicts(dict_1: dict, dict_2: dict) -> dict:
        combined_dict = dict_1 | dict_2
        return combined_dict

    '''
    The biggest incomes and expenses
    '''

    @staticmethod
    def max_value_from_dict(given_dict: dict) -> tuple:
        max_key = max(given_dict, key=given_dict.get)
        max_value = given_dict[max_key]
        return max_key, max_value

    def month_info(self, user_data: tuple, month: str) -> dict:
        self.cursor.execute(
            '''
            SELECT * FROM monthbudget 
            WHERE Username = %s 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) >= CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2)) 
            AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))
            ''',
            (user_data[0], month, month, self.get_current_month()[-1], self.get_current_month()[-1])
        )

        rows = self.cursor.fetchall()
        result_dict = {}

        for row in rows:
            month_name = row[1]  # Assuming the first column is 'Month'
            incomes = row[2]  # Assuming the second column is 'Incomes'
            expenses = row[3]  # Assuming the third column is 'Expenses'
            free_amount = row[4]  # Assuming the fourth column is 'FreeAmount'

            # Check if month_name already exists in result_dict
            if month_name not in result_dict:
                # If it doesn't exist, create a new entry
                result_dict[month_name] = [incomes, expenses, free_amount]
            else:
                # If it exists, append the new values (if needed)
                result_dict[month_name][0] += incomes  # Append incomes
                result_dict[month_name][1] += expenses  # Append expenses
                result_dict[month_name][2] += free_amount  # Append free amount

        return result_dict

    @staticmethod
    def operation_from_dict(month_data: dict, operation: str, value_type: int) -> Union[tuple, None]:
        if not month_data:  # Check if the dictionary is empty
            return None  # Or raise an exception, depending on your needs

        # Initialize variables based on the operation
        if operation == 'max':
            result = float('-inf')  # Initialize to negative infinity for max
            result_month = None
        else:  # operation == 'min'
            result = float('inf')  # Initialize to positive infinity for min
            result_month = None

        for month, values in month_data.items():
            value = values[value_type]  # Assuming the first element is incomes

            if operation == 'max' and value > result:
                result = value
                result_month = month
            elif operation == 'min' and value < result:
                result = value
                result_month = month

        return result_month, result  # Return as a tuple (month, income)

    @staticmethod
    def create_monthly_dict() -> dict:
        # Create a dictionary with months as keys and lists of Decimal('0.00') as values
        months_dict = {
            '01': Decimal('0.00'),  # January
            '02': Decimal('0.00'),  # February
            '03': Decimal('0.00'),  # March
            '04': Decimal('0.00'),  # April
            '05': Decimal('0.00'),  # May
            '06': Decimal('0.00'),  # June
            '07': Decimal('0.00'),  # July
            '08': Decimal('0.00'),  # August
            '09': Decimal('0.00'),  # September
            '10': Decimal('0.00'),  # October
            '11': Decimal('0.00'),  # November
            '12': Decimal('0.00')  # December
        }
        return months_dict

    @staticmethod
    def update_data(months_dict: dict, existing_data: dict, index: int):
        for month_key, values in existing_data.items():
            month, year = month_key.split('/')  # Split into month and year

            if month in months_dict:
                # Update the value at the specified index
                months_dict[month] += values[index]  # Add the value at the specified index

        return months_dict
