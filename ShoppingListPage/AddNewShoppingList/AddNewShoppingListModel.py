import mysql.connector
import pandas as pd
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
    @staticmethod
    def create_df() -> pd.DataFrame:
        items_df = pd.DataFrame(columns=["Item name", "Item quantity"])
        return items_df

    # Adding items to dataframe
    @staticmethod
    def add_items_to_df(item_name: str, item_quantity: str, items_df: pd.DataFrame) -> pd.DataFrame:
        new_row = {"Item name": item_name, "Item quantity": item_quantity}
        new_df = pd.DataFrame([new_row], index=[len(items_df)])
        updated_df = pd.concat([items_df, new_df], ignore_index=False)
        return updated_df

    # Delete selected item from dataframe
    @staticmethod
    def delete_from_df(item_name: str, items_df: pd.DataFrame) -> pd.DataFrame:
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        return items_df

    # Counts length of shopping list
    @staticmethod
    def length_of_dataframe(items_df: pd.DataFrame) -> int:
        num_rows = len(items_df.index)
        return num_rows

    # Adding shopping list to database
    def add_shopping_list_to_database(self, user_data: tuple, shopping_list_name: str, item_count: int, creation_date):
        insert_query = 'INSERT INTO shoppinglists (UserName, ListName, ListLength, CreationDate)' \
                       ' VALUES (%s, %s, %s, %s)'
        values_to_insert = (user_data[0], shopping_list_name, item_count, creation_date)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Gets shopping list id from database
    def get_shopping_list_id(self, shopping_list_name: str) -> int:
        self.cursor.execute('SELECT ListID FROM `shoppinglists` WHERE ListName = %s', (shopping_list_name,))
        row = self.cursor.fetchone()
        shopping_list_id = row[0]
        return shopping_list_id

    # Adding items from shopping list to database and assign it to shopping list id
    def add_items_to_database(self, shopping_list_id: int, user_data: tuple, items_df: pd.DataFrame):
        for index, row in items_df.iterrows():
            item, quantity = self.get_item_and_quantity(row)
            insert_query = 'INSERT INTO `shoppinglistitems` (ListID, Username, Item, Quantity)' \
                           ' VALUES (%s, %s, %s, %s)'
            values_to_insert = (shopping_list_id, user_data[0], item, quantity)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    # Gets item name and its price
    @staticmethod
    def get_item_and_quantity(row: pd.Series) -> tuple:
        name = row["Item name"]
        quantity = row["Item quantity"]

        return name, quantity

    # Get today's date
    @staticmethod
    def get_creation_time():
        creation_date = date.today()
        return creation_date

    # Get list of names from dataframe
    @staticmethod
    def get_names_from_items_df(items_df: pd.DataFrame) -> list:
        item_names = items_df['Item name'].tolist()
        return item_names
    '''
    UPDATE METHODS
    '''

    # Updates item count
    def update_item_count(self, item_count: int, shopping_list_id: int):
        self.cursor.execute('UPDATE `shoppinglists` SET ListLength = %s WHERE ListID = %s',
                            (item_count, shopping_list_id))
        self.connection.commit()

    # Delete old items from database before update
    def delete_items_from_database(self, shopping_list_id: int):
        self.cursor.execute('DELETE FROM `shoppinglistitems` WHERE ListID = %s', (shopping_list_id,))
        self.connection.commit()

    '''
    EDIT ELEMENT METHODS
    '''
    # Edits selected element in items_df then return updated df
    @staticmethod
    def edit_element_in_df(items_df: pd.DataFrame, old_name: str, new_name: str, new_quantity: float) -> pd.DataFrame:
        row_index = items_df.loc[items_df["Item name"] == old_name].index[0]
        items_df.loc[row_index, 'Item name'] = new_name
        items_df.loc[row_index, "Item quantity"] = float(new_quantity)

        return items_df
