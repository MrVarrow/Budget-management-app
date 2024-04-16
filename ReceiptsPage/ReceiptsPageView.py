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
        self.overview_frame.grid(row=1, rowspan=4, column=1, sticky=W)

        # Labels
        Label(self.receipts_frame, text="Receipts page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=250, pady=40, ipadx=210, ipady=50)

        Label(self.receipts_frame, text="Your receipts:", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=100)

        # Combobox
        ttk.Combobox(self.receipts_frame, font=('Arial', 20))\
            .grid(row=2, column=0, sticky=W, padx=100)

        # Choose receipt button
        Button(self.receipts_frame, text="Choose", font=('Arial', 20), bg='light gray', width=10, command=lambda: controller.choose_receipt()) \
            .grid(row=3, column=0, sticky=W, padx=170, pady=20)

        # Delete receipt button
        Button(self.receipts_frame, text="Delete", font=('Arial', 20), bg='light gray', width=10, command=lambda: controller.delete_receipt()) \
            .grid(row=4, column=0, sticky=W, padx=170, pady=30)

        # Add new receipt button
        Button(self.receipts_frame, text="Add new receipt", font=('Arial', 20), bg='light gray', width=15, command=lambda: controller.add_new_receipt()) \
            .grid(row=5, column=0, sticky=W, padx=130)

        # Back to logged user page button
        Button(self.receipts_frame, text="Back", font=('Arial', 15), bg='light gray', width=7, command=lambda: controller.back_to_logged_user_page()) \
            .grid(row=6, column=1, columnspan=2, sticky=SE, pady=30, padx=10)

        # Overview frame


        table = ttk.Treeview(self.overview_frame, height=15)
        table.column("#0", width=300)
        table.grid(sticky=E)

    def destroy_receipts_page_frame(self):
        self.receipts_frame.destroy()
