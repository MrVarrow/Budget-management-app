import mysql.connector
import re
import pandas as pd


# solveproblem with delete
class ManageConstBudgetModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

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

    def add_items_to_database(self, user_data, incomes_df, expenses_df):
        for index, row in incomes_df.iterrows():
            category, amount = self.get_category_and_amount(row)
            insert_query = ''
            values_to_insert = ()
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()
        for index, row in expenses_df.iterrows():
            category, amount = self.get_category_and_amount(row)
            insert_query = ''
            values_to_insert = ()
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

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
        ...

    def calculate_total_expenses(self, expenses_df):
        ...

    def calculate_free_amount(self, total_incomes, total_expenses):
        free = float(total_incomes) - float(total_expenses)
        return free



