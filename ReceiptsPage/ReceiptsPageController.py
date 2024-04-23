from tkinter import messagebox
from ReceiptsPage.ReceiptsPageView import ReceiptsPageView
from ReceiptsPage.ReceiptsPageModel import ReceiptsPageModel


class ReceiptsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.items_df = None

        self.receipts_page_model = ReceiptsPageModel()
        self.receipts_page_view = ReceiptsPageView(self.root, self, self.bg_color)
        self.receipts_page_view.receipt_combobox_update(
            self.receipts_page_model.receipt_list_from_database(self.user_data[0]))
        self.receipts_page_view.create_treeview(self.receipts_page_model.create_df())

    # Add new receipt button method
    def add_new_receipt(self):
        from ReceiptsPage.AddNewReceipt.AddNewReceiptController import AddNewReceiptController
        self.receipts_page_view.destroy_receipts_page_frame()
        AddNewReceiptController(self.root, self.user_data, self.bg_color, self.items_df, state="ADD", receipt_name=None)

    # Delete receipt button method
    def delete_receipt(self, receipt_name):
        result = messagebox.askquestion(title='Warning', message="Do you want to delete selected receipt?")
        if result == "yes":
            self.receipts_page_model.delete_receipt_from_database(receipt_name,
                                                                  self.receipts_page_model.select_receipt(receipt_name))

            self.receipts_page_view.clear_treeview()
            self.receipts_page_view.clear_receipt_data()
        elif result == "no":
            pass

    # Choose receipt button method
    def choose_receipt(self, receipt_name):
        receipt_id = self.receipts_page_model.select_receipt(receipt_name)
        self.items_df = self.receipts_page_model.items_from_receipt(receipt_id)
        receipt_date = self.receipts_page_model.receipt_date(receipt_id)
        total_price = self.receipts_page_model.total_price(receipt_id)

        self.receipts_page_view.clear_treeview()
        self.receipts_page_view.clear_receipt_data()
        self.receipts_page_view.add_items_to_treeview(self.items_df)
        self.receipts_page_view.display_receipt_data(total_price, receipt_name, receipt_date)

    # Edit receipt button method
    def edit_receipt(self, receipt_name):
        if self.receipts_page_model.check_chosen_receipt(receipt_name):
            from ReceiptsPage.AddNewReceipt.AddNewReceiptController import AddNewReceiptController
            self.receipts_page_view.destroy_receipts_page_frame()
            AddNewReceiptController(self.root, self.user_data, self.bg_color, self.items_df, state="UPDATE",
                                    receipt_name=receipt_name)
            return
        messagebox.showinfo(title="Information", message="You need to choose receipt for editing first")

    # Back to logged user page
    def back_to_logged_user_page(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)
