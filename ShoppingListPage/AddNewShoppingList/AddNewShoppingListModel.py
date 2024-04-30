import mysql.connector
import pandas as pd
import re
from datetime import date


class AddShoppingListModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    '''
    ADD METHODS
    '''

    # Crates empty df for treeview template
    def create_df(self):
        items_df = pd.DataFrame(columns=["Item name", "Item quantity"])
        return items_df

    # Adding items to dataframe
    def add_items_to_df(self, item_name, item_quantity, items_df):
        new_row = {"Item name": item_name, "Item quantity": item_quantity}
        new_df = pd.DataFrame([new_row], index=[len(items_df)])
        updated_df = pd.concat([items_df, new_df], ignore_index=False)
        return updated_df

    # Delete selected item from dataframe
    def delete_from_df(self, item_name, items_df):
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        return items_df

    # Counts length of shopping list
    def lenght_of_shopping_list(self, items_df):
        num_rows = len(items_df.index)
        return num_rows

    # Check if product name is correct
    def check_product_name(self, item_name):
        if re.search(r"\W", item_name) or re.search("[0-9]", item_name):
            return False
        return True

    # Check if product quantity is correct
    def check_product_quantity(self, item_quantity):
        if not re.search(r'^\d+(?:[.]\d{1,2,3}|$)$', item_quantity):
            return False
        return True

    # Check if shopping list name is correct
    def check_receipt_name(self, shopping_list_name):
        if re.search(r"\W", shopping_list_name):
            return False
        return True

    # Adding shopping list to database
    def add_shopping_list_to_database(self, user_data, shopping_list_name, item_count, creation_date):
        insert_query = 'INSERT INTO shoppinglists (UserName, ListName, ListLength, CreationDate)' \
                       ' VALUES (%s, %s, %s, %s)'
        values_to_insert = (user_data[0], shopping_list_name, item_count, creation_date)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Gets shopping list id from database
    def get_shopping_list_id(self, shopping_list_name):
        self.cursor.execute('SELECT ListID FROM `shoppinglists` WHERE ListName = %s', (shopping_list_name,))
        row = self.cursor.fetchone()
        shopping_list_id = row[0]
        return shopping_list_id

    # Adding items from shopping list to database and assign it to shopping list id
    def add_items_to_database(self, shopping_list_id, user_data, items_df):
        for index, row in items_df.iterrows():
            item, quantity = self.get_item_and_quantity(row)
            insert_query = 'INSERT INTO `shoppinglistitems` (ListID, Username, Item, Quantity)' \
                           ' VALUES (%s, %s, %s, %s)'
            values_to_insert = (shopping_list_id, user_data[0], item, quantity)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    # Gets item name and its price
    def get_item_and_quantity(self, row):
        name = row["Item name"]
        quantity = row["Item quantity"]

        return name, quantity

    # Get time of shopping list creation in system
    def get_creation_time(self):
        creation_date = date.today()
        return creation_date

    def check_for_duplicates(self):
        ...

    '''
    UPDATE METHODS
    '''

    # Updates item count
    def update_item_count(self, item_count, shopping_list_id):
        self.cursor.execute('UPDATE `shoppinglists` SET ListLength = %s WHERE ID = %s', (item_count, shopping_list_id))
        self.connection.commit()

    # Delete old items from database before update
    def delete_items_from_database(self, shopping_list_id):
        self.cursor.execute('DELETE FROM `shoppinglistitems` WHERE ListID = %s', (shopping_list_id,))
        self.connection.commit()

    '''
    EDIT ELEMENT METHODS
    '''

    def edit_element_in_df(self, items_df, old_name, new_name, new_quantity):
        row_index = items_df.loc[items_df["Item name"] == old_name].index[0]
        items_df.loc[row_index, 'Item name'] = new_name
        items_df.loc[row_index, "Item quantity"] = float(new_quantity)

        return items_df

