import mysql.connector
import pandas as pd


class AddShoppingListModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Crates empty df for treeview template
    def create_df(self):
        items_df = pd.DataFrame(columns=["Item name", "Item quantity"])
        return items_df
