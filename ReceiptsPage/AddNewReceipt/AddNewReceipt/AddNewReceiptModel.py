import mysql.connector
import pandas as pd
from tkinter import filedialog


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
        print(items_df)
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        print(items_df)
        return items_df

    # Choose file to photo via filedialog
    def choose_file(self):
        filepath = filedialog.askopenfilename()
        return filepath
