from ReceiptsPage.AddNewReceipt.AddNewReceiptModel import AddNewReceiptModel
from ReceiptsPage.AddNewReceipt.AddNewReceiptView import AddNewReceiptView
from tkinter import messagebox


class AddNewReceiptController:
    def __init__(self, root, user_data, bg_color, items_df, receipt_name, state):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.receipt_name = receipt_name

        self.add_new_receipt_model = AddNewReceiptModel()
        self.add_new_receipt_view = AddNewReceiptView(self.root, self, self.bg_color, self.receipt_name, state)
        if items_df is None:
            self.items_df = self.add_new_receipt_model.create_df()
            self.add_new_receipt_view.create_treeview(self.items_df)
        else:
            self.items_df = items_df
            self.add_new_receipt_view.create_treeview(self.items_df)
            self.add_new_receipt_view.update_treeview(self.items_df)

    # Submit item button method
    def submit_item(self, item_name, item_price):
        if not self.add_new_receipt_model.check_product_name(item_name):
            messagebox.showinfo(title="Information", message="Entered product name contains not allowed characters")
            return
        if not self.add_new_receipt_model.check_product_price(item_price):
            messagebox.showinfo(title="Information", message="Entered product price is incorrect or contains not "
                                                             "allowed characters please follow format: xx.xx or xx")
            return

        self.items_df = self.add_new_receipt_model.add_items_to_df(item_name, item_price, self.items_df)
        self.add_new_receipt_view.delete_items_in_treeview()
        self.add_new_receipt_view.update_treeview(self.items_df)

    # Delete selected item method
    def delete_item(self, item_name):
        try:
            result = messagebox.askquestion(title='Warning', message="Do you want to delete selected item from your "
                                                                     "receipt?")
            if result == "yes":
                self.items_df = self.add_new_receipt_model.delete_from_df(item_name, self.items_df)
                self.add_new_receipt_view.delete_items_in_treeview()
                self.add_new_receipt_view.update_treeview(self.items_df)
            elif result == "no":
                pass
        except IndexError:
            messagebox.showinfo(title="Information", message="Please select item to delete first, by clicking on it.")

    # Add receipt to database
    def add_receipt(self, receipt_name):
        if not self.add_new_receipt_model.check_receipt_name(receipt_name):
            messagebox.showinfo(title="Information", message="Entered receipt name contains not allowed characters")
            return

        self.add_new_receipt_model.add_receipt_to_database(
            self.user_data, receipt_name,
            self.add_new_receipt_model.item_count_in_receipt(self.items_df),
            self.add_new_receipt_model.get_creation_time()
        )
        self.add_new_receipt_model.add_items_to_database(
            self.add_new_receipt_model.get_receipt_id(receipt_name),
            self.user_data,
            self.items_df,
            self.add_new_receipt_model.calculate_total_price(self.items_df),
        )
        self.add_new_receipt_view.reset_receipt()
        self.items_df = self.add_new_receipt_model.create_df()
        messagebox.showinfo(title="Information", message="Receipt has been added successfully!")

    # Update receipt button method
    def update_receipt(self):
        self.add_new_receipt_model.delete_items_from_database(self.add_new_receipt_model.get_receipt_id(self.receipt_name))
        self.add_new_receipt_model.add_items_to_database(
            self.add_new_receipt_model.get_receipt_id(self.receipt_name),
            self.user_data,
            self.items_df,
            self.add_new_receipt_model.calculate_total_price(self.items_df)
        )
        self.add_new_receipt_model.update_item_count(
            self.add_new_receipt_model.item_count_in_receipt(self.items_df),
            self.add_new_receipt_model.get_receipt_id(self.receipt_name)
        )

        self.back_to_receipt_page()
        messagebox.showinfo(title="Information", message="Receipt has been updated successfully!")

    # Choosing path to photo method
    def choose_path_to_photo(self):
        filepath = self.add_new_receipt_model.choose_file()
        self.add_new_receipt_view.configure_file_path_view(filepath)

    def submit_photo(self, filepath):
        # proceed ocr and ML
        results = self.add_new_receipt_model.preprocess_receipt_image(filepath)
        self.add_new_receipt_model.look_for_products(results)

    # Clearing receipt local data if user wants to start over
    def clear_receipt_data(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to clear receipt, "
                                                                 "your progress with adding receipt will be lost")
        if result == "yes":
            self.items_df = self.add_new_receipt_model.create_df()
            self.add_new_receipt_view.clear_treeview()
        elif result == "no":
            pass

    # Back to receipt page method
    def back_to_receipt_page(self):
        from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
        ReceiptsPageController(self.root, self.user_data, self.bg_color)
