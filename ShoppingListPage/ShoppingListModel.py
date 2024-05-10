import mysql.connector
import pandas as pd


class ShoppingListModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Gets list of user shopping list from database
    def shopping_list_list_from_database(self, username):
        self.cursor.reset()
        self.cursor.execute('SELECT ListName FROM `shoppinglists` WHERE Username = %s', (username,))
        rows = self.cursor.fetchall()
        list_of_receipts = []
        for row in rows:
            list_of_receipts.append(row[0])
        return list_of_receipts

    # Returning shopping list ID that user picked
    def select_shopping_list(self, shopping_list_name):
        self.cursor.reset()
        self.cursor.execute('SELECT ListID FROM `shoppinglists` WHERE ListName = %s', (shopping_list_name,))
        row = self.cursor.fetchone()
        return row[0]

    # Get shopping list creation date from database
    def shopping_list_date(self, shopping_list_id):
        self.cursor.reset()
        self.cursor.execute('SELECT CreationDate FROM `shoppinglists` WHERE ListID = %s', (shopping_list_id,))
        row = self.cursor.fetchone()
        return row[0]

    # Get shopping list items from database and save it do dataframe
    def items_from_shopping_list(self, shopping_list_id):
        self.cursor.reset()
        self.cursor.execute('SELECT Item, Quantity FROM `shoppinglistitems` WHERE ListID = %s', (shopping_list_id,))
        rows = self.cursor.fetchall()
        items_df = pd.DataFrame(rows, columns=["Item name", "Item quantity"])
        return items_df

    # Deletes shopping list from database
    def delete_shopping_list_from_database(self, shopping_list_name, shopping_list_id):
        self.cursor.execute('DELETE FROM `shoppinglistitems` WHERE ListID = %s', (shopping_list_id,))
        self.connection.commit()
        self.cursor.execute('DELETE FROM `shoppinglists` WHERE ListName = %s', (shopping_list_name,))
        self.connection.commit()

    # Check if user selected a shopping list to edit
    def check_chosen_shopping_list(self, chosen_list):
        if not chosen_list == "":
            return True
        return False

    # Check if shopping list is complete
    def check_completion(self, checkbox_list):
        if False in checkbox_list:
            return False
        return True

    # Toggle selected checkbutton and update its value in list
    def toggle_checkbutton(self, index, check_vars):
        for i, var in enumerate(check_vars):
            if i == index:
                if check_vars[i]:
                    check_vars[i] = False
                    break

                check_vars[i] = True

        return check_vars

