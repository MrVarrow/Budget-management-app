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
        ...

    '''
    General stats
    '''

