import mysql.connector
from datetime import datetime


class ManageBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    @staticmethod
    def get_12_months() -> list:
        months = []
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year
        for i in range(12):
            # Calculate the month and year for the current iteration
            month = (current_month + i - 1) % 12 + 1
            year = current_year + ((current_month + i - 1) // 12)

            # Format the month and year as a string
            month_str = str(month).zfill(2)
            year_str = str(year)
            month_year = f"{month_str}/{year_str}"

            # Add the month and year to the list
            months.append(month_year)
        return months

    def get_info_about_budget(self, username: str, date: str) -> tuple:
        self.cursor.reset()
        self.cursor.execute('SELECT * FROM `monthbudget` WHERE Username = %s AND Month = %s', (username, date))
        row = self.cursor.fetchone()
        incomes, expenses, free_amount = None, None, None
        if row:
            incomes = row[2]
            expenses = row[3]
            free_amount = row[4]

        return incomes, expenses, free_amount

    def get_info_about_const_budget(self, user_data: tuple) -> tuple:
        self.cursor.execute('SELECT * FROM `constbudget` WHERE Username = %s', (user_data[0],))
        row = self.cursor.fetchone()
        incomes, expenses, free_amount = None, None, None
        if row:
            incomes = row[1]
            expenses = row[2]
            free_amount = row[3]

        return incomes, expenses, free_amount

    def delete_budget_month(self, user_data: tuple, month: str):
        self.cursor.execute('DELETE FROM `monthbudget` WHERE Username = %s AND Month = %s', (user_data[0], month))
        self.connection.commit()

    def delete_budget_transactions(self, user_data: tuple, month: str):
        self.cursor.execute(
            'DELETE FROM `budgettransactions` WHERE Username = %s AND Month = %s', (user_data[0], month)
        )
        self.connection.commit()
