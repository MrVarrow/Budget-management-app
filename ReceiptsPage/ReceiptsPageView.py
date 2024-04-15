from tkinter import *
from tkinter import ttk


class ReceiptsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Receipts page frame
        self.receipts_frame = Frame(self.root)
        self.receipts_frame.grid(row=0, column=0)

        # Overview of receipt frame
        self.overview_frame = Frame(self.receipts_frame)
        self.overview_frame.grid(row=1, rowspan=4, column=1)

        # Labels
        Label(self.receipts_frame, text="Receipts page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)

        Label(self.receipts_frame, text="Your receipts:", font=('Arial', 15)) \
            .grid(row=1, column=0)

        # Combobox
        ttk.Combobox(self.receipts_frame)\
            .grid(row=2, column=0)

        # Choose receipt button
        Button(self.receipts_frame, text="Choose", font=('Arial', 20), bg='light gray', command=lambda: controller.choose_receipt()) \
            .grid(row=3, column=0)

        # Delete receipt button
        Button(self.receipts_frame, text="Delete", font=('Arial', 20), bg='light gray', command=lambda: controller.delete_receipt()) \
            .grid(row=4, column=0)

        # Add new receipt button
        Button(self.receipts_frame, text="Add new receipt", font=('Arial', 20), bg='light gray', command=lambda: controller.add_new_receipt()) \
            .grid(row=5, column=0)

        # Back to logged user page button
        Button(self.receipts_frame, text="Back", font=('Arial', 20), bg='light gray', command=lambda: controller.back_to_logged_user_page()) \
            .grid(row=6, column=1, sticky=SE)

        # Overview frame
        Label(self.overview_frame, text="data").grid()

    def destroy_receipts_page_frame(self):
        self.receipts_frame.destroy()
