from ReceiptsPage.AddNewReceipt.AddNewReceiptModel import AddNewReceiptModel
from ReceiptsPage.AddNewReceipt.AddNewReceiptView import AddNewReceiptView
from tkinter import messagebox


class AddNewReceiptController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.add_new_receipt_model = AddNewReceiptModel()
        self.add_new_receipt_view = AddNewReceiptView(self.root, self, self.bg_color)
        self.items_df = self.add_new_receipt_model.create_df()
        self.add_new_receipt_view.create_treeview(self.items_df)

    # Submit item button method
    def submit_item(self, item_name, item_price):
        self.items_df = self.add_new_receipt_model.add_items_to_df(item_name, item_price, self.items_df)
        self.add_new_receipt_view.delete_items_in_treeview()
        self.add_new_receipt_view.update_treeview(self.items_df)

    # Delete selected item method
    def delete_item(self, item_name):
        self.items_df = self.add_new_receipt_model.delete_from_df(item_name, self.items_df)
        self.add_new_receipt_view.delete_items_in_treeview()
        self.add_new_receipt_view.update_treeview(self.items_df)

    # Add receipt to database
    def add_receipt(self):
        # Add data from df to database
        ...

    # Choosing path to photo method
    def choose_path_to_photo(self):
        filepath = self.add_new_receipt_model.choose_file()
        self.add_new_receipt_view.configure_file_path_view(filepath)

    def submit_photo(self):
        # proceed ocr and ML
        ...

    # Back to receipt page method
    def back_to_receipt_page(self):
        from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
        ReceiptsPageController(self.root, self.user_data, self.bg_color)

