import mysql.connector
from datetime import datetime
from dateutil.relativedelta import relativedelta
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


    def get_current_month(self):
        current_date = datetime.now()
        formatted_month_year = current_date.strftime("%m/%Y")

        return [formatted_month_year]


    def get_time_period_in_int(self, time_period):
        time_period_dict = {"Last Month": 1, "Last 6 Months": 6, "Last Year": 12, "Last 5 Years": 60,
                            "Last 10 Years": 120, "All time": "*"}

        return time_period_dict[time_period]

    def get_list_of_months(self, time_period):
        today = datetime.today()

        months = []

        start_date = today - relativedelta(months=1)

        for i in range(time_period):
            # Calculate the month and year
            month_date = start_date - relativedelta(months=i)
            formatted_month = month_date.strftime("%m/%Y")
            months.append(formatted_month)
        print(months)
        return months

    def get_budget_month_info(self, user_data, month):
        months_info = []
        print(month)

        if month == self.get_current_month()[-1]:
            self.cursor.execute(
                'SELECT * FROM monthbudget WHERE Username = %s AND CONCAT(SUBSTRING(Month, 4, 4), SUBSTRING(Month, 1, 2)) < CONCAT(SUBSTRING(%s, 4, 4), SUBSTRING(%s, 1, 2))',
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


    def add_all_values(self, months_info):
        combined_values = [sum(values) for values in zip(*months_info)]
        return combined_values


    '''
    General stats
    '''

    def get_categories_for_expenses(self, user_data):
        list_of_expenses_categories = []
        self.cursor.execute('SELECT Category FROM budgettransactions WHERE username = %s AND type = %s ', (user_data[0], "Expense"))
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



    def get_categories_for_incomes(self, user_data):
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

    def get_values_from_database(self, user_data, type, category, month):
        if type == "spent":
            type_info = "Expense"
        elif type == "earned":
            type_info = "Income"
        print(type)
        print(category)
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
            (user_data[0], type_info, category, month, month, self.get_current_month()[-1], self.get_current_month()[-1]))
        rows = self.cursor.fetchall()
        print(rows)
        if not rows is None:
            for row in rows:
                list_of_values.append(row[0])
        self.cursor.reset()

        self.cursor.execute('SELECT Amount FROM consttransactions WHERE username = %s AND Type = %s AND Category = %s',
                            (user_data[0], type_info, category))
        rows = self.cursor.fetchall()
        print(rows)
        if not rows is None:
            for row in rows:
                list_of_values.append(row[0])
                print(list_of_values)
        return list_of_values

    def calculate_sum_of_values(self, values: list):
        return sum(values)

