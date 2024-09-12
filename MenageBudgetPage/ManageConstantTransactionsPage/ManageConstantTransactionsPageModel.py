import mysql.connector
import re
import pandas as pd
from datetime import datetime


class ManageConstBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def get_budget_from_db(self, user_data):
        self.cursor.execute(
            'SELECT * FROM consttransactions WHERE Username = %s', (user_data[0],)
        )
        rows = self.cursor.fetchall()
        return rows

    def update_budget(self, month, total_incomes, total_expenses, free_amount):
        update_query = 'UPDATE monthbudget SET Incomes = %s, Expenses = %s, FreeAmount = %s WHERE Month = %s'
        values_to_update = (total_incomes, total_expenses, free_amount, month)
        self.cursor.execute(update_query, values_to_update)
        self.connection.commit()

    def get_budget_info_df(self, sql_outcome):
        df = pd.DataFrame(sql_outcome, columns=[col[0] for col in self.cursor.description])
        income_mask = df['Type'] == 'Income'
        expense_mask = df['Type'] != 'Income'

        income_df = df.loc[income_mask, ['Category', 'Amount']].reset_index(drop=True)
        expense_df = df.loc[expense_mask, ['Category', 'Amount']].reset_index(drop=True)

        return income_df, expense_df

    def create_df(self):
        incomes_df = pd.DataFrame(columns=["Category", "Amount"])
        expenses_df = pd.DataFrame(columns=["Category", "Amount"])
        return incomes_df, expenses_df

    def add_items_to_incomes(self, category, amount, incomes_df):
        new_row = {"Category": category, "Amount": amount}
        new_df = pd.DataFrame([new_row], index=[len(incomes_df)])
        updated_df = pd.concat([incomes_df, new_df], ignore_index=False)
        return updated_df

    def add_items_to_expenses(self, category, amount, expenses_df):
        new_row = {"Category": category, "Amount": amount}
        new_df = pd.DataFrame([new_row], index=[len(expenses_df)])
        updated_df = pd.concat([expenses_df, new_df], ignore_index=False)
        return updated_df

    def delete_from_incomes_df(self, index, incomes_df):
        incomes_df.drop(index=index, inplace=True)
        items_df = incomes_df.reset_index(drop=True)
        return items_df

    def delete_from_expenses_df(self, index, expenses_df):
        expenses_df.drop(index=index, inplace=True)
        items_df = expenses_df.reset_index(drop=True)
        return items_df

    def insert_items_to_database(self, user_data, incomes_df, expenses_df):
        for index, row in incomes_df.iterrows():
            category, amount = self.get_category_and_amount(row)
            insert_query = 'INSERT INTO consttransactions (Username, Type, Category, Amount) VALUES (%s, %s, %s, %s)'
            values_to_insert = (user_data[0], 'Income', category, amount)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()
        for index, row in expenses_df.iterrows():
            category, amount = self.get_category_and_amount(row)
            insert_query = 'INSERT INTO consttransactions (Username, Type, Category, Amount) VALUES (%s, %s, %s, %s)'
            values_to_insert = (user_data[0], 'Expense', category, amount)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    def delete_items_from_database(self, user_data):
        self.cursor.execute('DELETE FROM consttransactions WHERE Username = %s', (user_data[0],))

    def get_category_and_amount(self, row):
        category = row["Category"]
        amount = row["Amount"]
        return category, amount

    def check_amount(self, amount):
        if not re.search(r'^\d+(?:[.]\d{1,2}|$)$', amount):
            return False
        return True

    def check_category(self, category):
        if not category == "":
            return False
        return True

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

    def check_if_budget_exists(self, user_data):
        self.cursor.execute('SELECT Incomes FROM `constbudget` WHERE Username = %s', (user_data[0],))
        row = self.cursor.fetchone()
        if row is None:
            return False
        return True

    def insert_budget(self, user_data, total_incomes, total_expenses, free_amount):
        insert_query = 'INSERT INTO constbudget (Username, Incomes, Expenses, FreeAmount) VALUES (%s, %s, %s, %s)'
        values_to_insert = (user_data[0], total_incomes, total_expenses, free_amount)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    def update_budget(self, user_data, total_incomes, total_expenses, free_amount):
        update_query = 'UPDATE constbudget SET Incomes = %s, Expenses = %s, FreeAmount = %s WHERE Username = %s'
        values_to_update = (total_incomes, total_expenses, free_amount, user_data[0])
        self.cursor.execute(update_query, values_to_update)
        self.connection.commit()





