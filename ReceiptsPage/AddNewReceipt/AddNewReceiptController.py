from ReceiptsPage.AddNewReceipt.AddNewReceiptModel import AddNewReceiptModel
from ReceiptsPage.AddNewReceipt.AddNewReceiptView import AddNewReceiptView
from tkinter import messagebox


class AddNewReceiptController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.add_new_receipt_view = AddNewReceiptView(self.root, self, self.bg_color)
        self.add_new_receipt_model = AddNewReceiptModel()