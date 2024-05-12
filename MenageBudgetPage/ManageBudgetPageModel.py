import mysql.connector
import pandas as pd
from datetime import datetime, timedelta


class ManageBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def get_12_months(self):
        months = []
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year
        for i in range(12):
            # Calculate the month and year for the current iteration
            month = (current_month + i) % 12
            year = current_year + ((current_month + i) // 12)

            # Format the month and year as a string
            month_str = str(month).zfill(2)
            year_str = str(year)
            month_year = f"{month_str}/{year_str}"

            # Add the month and year to the list
            months.append(month_year)
        return months

