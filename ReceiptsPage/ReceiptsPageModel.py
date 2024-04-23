import mysql.connector
import pandas as pd


class ReceiptsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Crates empty df for treeview template
    def create_df(self):
        items_df = pd.DataFrame(columns=["Item name", "Item price"])
        return items_df

    # Gets list of user receipts from database
    def receipt_list_from_database(self, username):
        self.cursor.reset()
        self.cursor.execute('SELECT ReceiptName FROM `receipts` WHERE UserName = %s', (username,))
        rows = self.cursor.fetchall()
        list_of_receipts = []
        for row in rows:
            list_of_receipts.append(row[0])
        return list_of_receipts

    # Returning Receipt ID that user picked
    def select_receipt(self, receipt_name):
        self.cursor.reset()
        self.cursor.execute('SELECT ReceiptID FROM `receipts` WHERE ReceiptName = %s', (receipt_name,))
        row = self.cursor.fetchone()
        return row[0]

    # Get receipts items from database and save it do dataframe
    def items_from_receipt(self, receipt_id):
        self.cursor.reset()
        self.cursor.execute('SELECT Item, Price FROM `receiptitems` WHERE ReceiptID = %s', (receipt_id,))
        rows = self.cursor.fetchall()
        items_df = pd.DataFrame(rows, columns=["Item name", "Item price"])
        return items_df

    # Get total price of receipt from database
    def total_price(self, receipt_id):
        self.cursor.reset()
        self.cursor.execute('SELECT TotalPrice FROM `receiptitems` WHERE ReceiptID = %s', (receipt_id,))
        row = self.cursor.fetchone()
        return row[0]

    # Get receipt creation date from database
    def receipt_date(self, receipt_id):
        self.cursor.reset()
        self.cursor.execute('SELECT CreationDate FROM `receipts` WHERE ReceiptID = %s', (receipt_id,))
        row = self.cursor.fetchone()
        return row[0]

    # Deletes receipt from database
    def delete_receipt_from_database(self, receipt_name, receipt_id):
        self.cursor.execute('DELETE FROM `receiptitems` WHERE ReceiptID = %s', (receipt_id,))
        self.connection.commit()
        self.cursor.execute('DELETE FROM `receipts` WHERE ReceiptName = %s', (receipt_name,))
        self.connection.commit()

    # Check if user selected a receipt to edit
    def check_chosen_receipt(self, chosen_receipt):
        if not chosen_receipt == "":
            return True
        return False

