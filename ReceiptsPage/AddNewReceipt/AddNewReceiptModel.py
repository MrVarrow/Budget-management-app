import mysql.connector
import pandas as pd
from tkinter import filedialog
import re


class AddNewReceiptModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Creating base of dataframe
    def create_df(self):
        items_df = pd.DataFrame(columns=["Item name", "Item price"])
        return items_df

    # Adding items to dataframe
    def add_items_to_df(self, item_name, item_price, items_df):
        new_row = {"Item name": item_name, "Item price": item_price}
        new_df = pd.DataFrame([new_row], index=[len(items_df)])
        updated_df = pd.concat([items_df, new_df], ignore_index=False)
        return updated_df

    # Delete selected item from dataframe
    def delete_from_df(self, item_name, items_df):
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        return items_df

    # Choose file to photo via filedialog
    def choose_file(self):
        filepath = filedialog.askopenfilename()
        return filepath

    # Counts number of items in receipt
    def item_count_in_receipt(self, items_df):
        num_rows = len(items_df.index)
        return num_rows

    # Calculates total price of receipt
    def calculate_total_price(self, items_df):
        prices = items_df['Item price'].tolist()
        total = 0
        for price in prices:
            total += float(price)
        return total

    # Adding receipt to database
    def add_receipt_to_database(self, user_data, receipt_name, item_count):
        insert_query = 'INSERT INTO `receipts` (UserName, ReceiptName, ItemsCount) VALUES (%s, %s, %s)'
        values_to_insert = (user_data[0], receipt_name, str(item_count))
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Gets receipt id from database
    def get_receipt_id(self, receipt_name):
        self.cursor.execute('SELECT ReceiptID FROM `receipts` WHERE ReceiptName = %s', (receipt_name,))
        row = self.cursor.fetchone()
        receipt_id = row[0]
        return receipt_id

    # Adding items from receipt to database and assign it to receipt id
    def add_items_to_database(self, receipt_id, user_data, items_df, total):
        for index, row in items_df.iterrows():
            item, price = self.get_items_and_prices(row)
            insert_query = 'INSERT INTO `receiptitems` (ReceiptID, Username, Item, Price, TotalPrice) VALUES (%s, %s, %s, %s, %s)'
            values_to_insert = (receipt_id, user_data[0], item, price, total)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    # Gets item name and its price
    def get_items_and_prices(self, row):
        name = row["Item name"]
        price = row["Item price"]

        return name, price

    # Check if product name is correct
    def check_product_name(self, item_name):
        if re.search(r"\W", item_name) or re.search("[0-9]", item_name):
            return False
        return True

    # Check if product price is correct
    def check_product_price(self, item_price):
        if not re.search(r'^\d+(?:[.]\d{1,2}|$)$', item_price):
            return False
        return True

    # Check if receipt name is correct
    def check_receipt_name(self, receipt_name):
        if re.search(r"\W", receipt_name):
            return False
        return True
