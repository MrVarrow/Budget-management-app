from tkinter import messagebox
from ReceiptsPage.ReceiptsPageView import ReceiptsPageView
from ReceiptsPage.ReceiptsPageModel import ReceiptsPageModel


# Maybe add editing option in future
# passing to add new receipt window then when user want to add receipt check if exists by ID and update it in db or simply new page
class ReceiptsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.receipts_page_model = ReceiptsPageModel()
        self.receipts_page_view = ReceiptsPageView(self.root, self, self.bg_color)
        self.receipts_page_view.receipt_combobox_update(
            self.receipts_page_model.receipt_list_from_database(self.user_data[0]))
        self.receipts_page_view.create_treeview(self.receipts_page_model.create_df())

    def add_new_receipt(self):
        from ReceiptsPage.AddNewReceipt.AddNewReceiptController import AddNewReceiptController
        self.receipts_page_view.destroy_receipts_page_frame()
        AddNewReceiptController(self.root, self.user_data, self.bg_color)

    def delete_receipt(self, receipt_name):
        result = messagebox.askquestion(title='Warning', message="Do you want to delete selected receipt?")
        if result == "yes":
            self.receipts_page_model.delete_receipt_from_database(receipt_name,
                                                                  self.receipts_page_model.select_receipt(receipt_name))

            self.receipts_page_view.clear_treeview()
            self.receipts_page_view.clear_total_price()
        elif result == "no":
            pass

    def choose_receipt(self, receipt_name):
        items_df = self.receipts_page_model.items_from_receipt(
            self.receipts_page_model.select_receipt(receipt_name))

        self.receipts_page_view.clear_treeview()
        self.receipts_page_view.clear_total_price()
        self.receipts_page_view.add_items_to_treeview(items_df)
        self.receipts_page_view.display_total_price(
            self.receipts_page_model.total_price(self.receipts_page_model.select_receipt(receipt_name)))

    def back_to_logged_user_page(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)
