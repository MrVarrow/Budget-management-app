from tkinter import messagebox
from ReceiptsPage.ReceiptsPageView import ReceiptsPageView
from ReceiptsPage.ReceiptsPageModel import ReceiptsPageModel


class ReceiptsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.receipts_page_view = ReceiptsPageView(self.root, self, self.bg_color)
        self.receipts_page_model = ReceiptsPageModel()

    def add_new_receipt(self):
        from ReceiptsPage.AddNewReceipt.AddNewReceiptController import AddNewReceiptController
        self.receipts_page_view.destroy_receipts_page_frame()
        AddNewReceiptController(self.root, self.user_data, self.bg_color)

    def delete_receipt(self):
        ...

    def choose_receipt(self):
        ...

    def back_to_logged_user_page(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        LoggedUserPageController(self.root, self.user_data, self.bg_color)
