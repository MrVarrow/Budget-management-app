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

    def delete_item(self, selected_item):
        # Delete item from df then update treeview
        print(selected_item)
        self.add_new_receipt_view.delete_item_from_treeview(selected_item)

    def add_receipt(self):
        # Add data from df to database
        ...

    def choose_path_to_photo(self):
        # File browser
        ...

    def submit_photo(self):
        # proceed ocr and ML
        ...

    def back_to_receipt_page(self):
        from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
        ReceiptsPageController(self.root, self.user_data, self.bg_color)

