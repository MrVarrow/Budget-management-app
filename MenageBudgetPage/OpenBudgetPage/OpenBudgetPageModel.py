import mysql.connector
import pandas as pd


class OpenBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def get_budget_from_db(self, user_data, month):
        self.cursor.execute(
            'SELECT * FROM budgettransactions WHERE Username = %s AND Month = %s', (user_data[0], month)
        )
        rows = self.cursor.fetchall()
        return rows

    def create_df(self):
        incomes_df = pd.DataFrame(columns=["Category", "Amount"])
        expenses_df = pd.DataFrame(columns=["Category", "Amount"])
        return incomes_df, expenses_df

    def budget_into_df(self, sql_outcome):
        df = pd.DataFrame(sql_outcome, columns=[col[0] for col in self.cursor.description])
        income_mask = df['Type'] == 'Income'
        expense_mask = df['Type'] != 'Income'

        income_df = df.loc[income_mask, ['Category', 'Amount']].reset_index(drop=True)
        expense_df = df.loc[expense_mask, ['Category', 'Amount']].reset_index(drop=True)

        return income_df, expense_df

    def get_const_from_db(self, user_data):
        self.cursor.execute('SELECT * FROM consttransactions WHERE Username = %s', (user_data[0],))
        rows = self.cursor.fetchall()
        return rows

    def const_budget_into_df(self, sql_outcome):
        df = pd.DataFrame(sql_outcome, columns=[col[0] for col in self.cursor.description])

        income_mask = df['Type'] == 'Income'
        expense_mask = df['Type'] != 'Income'

        const_incomes_df = df.loc[income_mask, ['Category', 'Amount']].reset_index(drop=True)
        const_expenses_df = df.loc[expense_mask, ['Category', 'Amount']].reset_index(drop=True)
        return const_incomes_df, const_expenses_df

    def add_dfs(self, df1, df2):
        combined_df = pd.concat([df1, df2], ignore_index=True)
        return combined_df

    def calculate_total_incomes(self, incomes_df):
        income_values = incomes_df["Amount"].values.tolist()
        total_income = 0
        for amount in income_values:
            total_income += float(amount)
        return total_income

    def calculate_total_expenses(self, expenses_df):
        expenses_values = expenses_df["Amount"].values.tolist()
        total_expenses = 0
        for amount in expenses_values:
            total_expenses += float(amount)
        return total_expenses

    def calculate_free_amount(self, total_incomes, total_expenses):
        free = float(total_incomes) - float(total_expenses)
        return free
