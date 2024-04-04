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
