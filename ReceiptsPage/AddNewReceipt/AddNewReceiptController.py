from ReceiptsPage.AddNewReceipt.AddNewReceiptModel import AddNewReceiptModel
from ReceiptsPage.AddNewReceipt.AddNewReceiptView import AddNewReceiptView
from tkinter import messagebox
from Validations.Validations import special_character_in_string, correct_price_format, digits_in_string


class AddNewReceiptController:
    def __init__(self, root, user_data, bg_color, items_df, list_of_user_receipts, receipt_name, state):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.receipt_name = receipt_name
        self.list_of_user_receipts = list_of_user_receipts

        self.add_new_receipt_model = AddNewReceiptModel()
        self.add_new_receipt_view = AddNewReceiptView(self.root, self, self.bg_color, self.receipt_name, state)
        if items_df is None:
            self.items_df = self.add_new_receipt_model.create_df()
            self.add_new_receipt_view.create_treeview(self.items_df)
        else:
            self.items_df = items_df
            self.add_new_receipt_view.create_treeview(self.items_df)
            self.add_new_receipt_view.update_treeview(self.items_df)

    def submit_item(self, item_name: str, item_price: str):
        if digits_in_string(item_name) or special_character_in_string(item_name):
            messagebox.showinfo("Information", "Entered product name contains not allowed characters")
            return
        if not correct_price_format(item_price):
            messagebox.showinfo("Information", "Entered product price is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return
        self.items_df = self.add_new_receipt_model.add_items_to_df(item_name, item_price, self.items_df)
        self.add_new_receipt_view.delete_items_in_treeview()
        self.add_new_receipt_view.update_treeview(self.items_df)

    def delete_item(self, item_name: str):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your receipt?")
            if result == "yes":
                self.items_df = self.add_new_receipt_model.delete_from_df(item_name, self.items_df)
                self.add_new_receipt_view.delete_items_in_treeview()
                self.add_new_receipt_view.update_treeview(self.items_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")

    def add_receipt(self, receipt_name: str):
        if special_character_in_string(receipt_name):
            messagebox.showinfo("Information", "Entered receipt name contains not allowed characters")
            return

        if self.add_new_receipt_model.check_for_duplicates(receipt_name, self.list_of_user_receipts):
            messagebox.showinfo("Information", "This Receipt name already exists.")
            return

        self.add_new_receipt_model.add_receipt_to_database(
            self.user_data, receipt_name,
            self.add_new_receipt_model.item_count_in_receipt(self.items_df),
            self.add_new_receipt_model.get_creation_time()
        )
        receipt_id = self.add_new_receipt_model.get_receipt_id(receipt_name)
        self.add_new_receipt_model.add_items_to_database(
            receipt_id,
            self.user_data,
            self.items_df,
            self.add_new_receipt_model.calculate_total_price(self.items_df)
        )
        self.add_new_receipt_view.reset_receipt()
        self.items_df = self.add_new_receipt_model.create_df()
        messagebox.showinfo("Information", "Receipt has been added successfully!")

    def update_receipt(self):
        receipt_id = self.add_new_receipt_model.get_receipt_id(self.receipt_name)
        self.add_new_receipt_model.delete_items_from_database(receipt_id)
        self.add_new_receipt_model.add_items_to_database(
            receipt_id,
            self.user_data,
            self.items_df,
            self.add_new_receipt_model.calculate_total_price(self.items_df)
        )
        self.add_new_receipt_model.update_item_count(
            self.add_new_receipt_model.item_count_in_receipt(self.items_df),
            receipt_id
        )
        self.back_to_receipt_page()
        messagebox.showinfo("Information", "Receipt has been updated successfully!")

    def choose_path_to_photo(self):
        self.add_new_receipt_view.configure_file_path_view(self.add_new_receipt_model.choose_file())

    def submit_photo(self, filepath: str):
        results = self.add_new_receipt_model.preprocess_receipt_image(filepath)
        prod = self.add_new_receipt_model.look_for_products(results)
        price = self.add_new_receipt_model.look_for_prices(results)
        self.items_df = self.add_new_receipt_model.dict_to_df(
            self.add_new_receipt_model.create_dict(prod, price)
        )
        self.add_new_receipt_view.update_treeview(self.items_df)

    def clear_receipt_data(self):
        result = messagebox.askquestion("Warning", "Do you want to clear receipt, "
                                                   "your progress with adding receipt will be lost")
        if result == "yes":
            self.items_df = self.add_new_receipt_model.create_df()
            self.add_new_receipt_view.clear_treeview()

    def edit_element(self, item_value: str):
        self.add_new_receipt_view.edit_element_window(item_value[0], item_value[1])

    def back_to_receipt_page(self):
        from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
        self.add_new_receipt_view.destroy_add_new_receipt_frame()
        ReceiptsPageController(self.root, self.user_data, self.bg_color)

    '''
    EDIT ELEMENTS WINDOW METHODS
    '''

    def apply_edit(self, old_name: str, new_name: str, new_price: str):
        try:
            self.items_df = self.add_new_receipt_model.edit_element_in_df(self.items_df, old_name, new_name,
                                                                          float(new_price))
            self.add_new_receipt_view.edit_element_window_destroy()
            messagebox.showinfo("Information", "Receipt element has been updated successfully!")
            self.add_new_receipt_view.clear_treeview()
            self.add_new_receipt_view.update_treeview(self.items_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to edit it first, by clicking on it.")

    def discard_edit(self):
        self.add_new_receipt_view.edit_element_window_destroy()
