from tkinter import *
from tkinter import ttk


class ReceiptsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Variables
        self.combobox_var = StringVar()
        self.total_price = ""

        # Receipts page frame
        self.receipts_frame = Frame(self.root, bg=self.bg_color)
        self.receipts_frame.grid(row=0, column=0)

        # Overview of receipt frame
        self.overview_frame = Frame(self.receipts_frame, bg=self.bg_color)
        self.overview_frame.grid(row=1, rowspan=4, column=1, sticky=W)

        # Labels
        Label(self.receipts_frame, text="Receipts page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=250, pady=40, ipadx=230, ipady=50)

        Label(self.receipts_frame, text="Your receipts:", font=('Arial', 15), bg=self.bg_color) \
            .grid(row=1, column=0, sticky=W, padx=100)

        Label(self.receipts_frame, text="Total:", font=('Arial', 20), bg=self.bg_color) \
            .grid(row=5, column=1, sticky=W)

        self.total_price_widget = Label(self.receipts_frame, text=self.total_price, font=('Arial', 20),
                                        bg=self.bg_color)
        self.total_price_widget.grid(row=5, column=0, sticky=E, padx=250, columnspan=2)

        self.receipt_name_widget = Label(self.receipts_frame, text="", font=('Arial', 15), width=22, bg=self.bg_color)
        self.receipt_name_widget.grid(row=3, column=0, columnspan=2, sticky=W, padx=460)

        self.receipt_date_widget = Label(self.receipts_frame, text="", font=('Arial', 15), width=22, bg=self.bg_color)
        self.receipt_date_widget.grid(row=3, rowspan=2, column=0, columnspan=2, sticky=W, padx=460, pady=40)

        # Combobox
        self.combobox_receipts = ttk.Combobox(self.receipts_frame, font=('Arial', 20), textvariable=self.combobox_var)
        self.combobox_receipts.grid(row=2, column=0, sticky=W, padx=100)

        # Choose receipt button
        Button(self.receipts_frame, text="Choose", font=('Arial', 20), bg='light gray', width=15,
               command=lambda: controller.choose_receipt(self.combobox_var.get())) \
            .grid(row=3, column=0, sticky=W, padx=130, pady=20)

        # Delete receipt button
        Button(self.receipts_frame, text="Delete Receipt", font=('Arial', 20), bg='light gray', width=15,
               command=lambda: controller.delete_receipt(self.combobox_var.get())) \
            .grid(row=4, column=0, sticky=W, padx=130, pady=30)

        # Add new receipt button
        Button(self.receipts_frame, text="Add new receipt", font=('Arial', 20), bg='light gray',
               width=15, command=lambda: controller.add_new_receipt()) \
            .grid(row=5, column=0, sticky=W, padx=130)

        # Edit receipt button
        Button(self.receipts_frame, text="Edit Receipt", font=('Arial', 20), bg="light gray", width=15,
               command=lambda: controller.edit_receipt(self.receipt_name_widget.cget("text"))) \
            .grid(row=5, column=0, columnspan=2, sticky=W, padx=460)

        # Back to logged user page button
        Button(self.receipts_frame, text="Back", font=('Arial', 15), bg='light gray', width=7,
               command=lambda: controller.back_to_logged_user_page()) \
            .grid(row=6, column=1, columnspan=2, sticky=SE, pady=30, padx=30)

    # Overview receipt treeview
    def create_treeview(self, receipt_df):
        self.overview = ttk.Treeview(self.overview_frame, height=15)
        self.overview["columns"] = list(receipt_df.columns)
        self.overview.column("#0", width=50)
        for col in receipt_df.columns:
            self.overview.column(col, width=100)

        self.overview.heading("#0", text="Index", anchor="w")
        for col in receipt_df.columns:
            self.overview.heading(col, text=col, anchor="w")

        self.overview.pack(fill="both", expand=True, side=LEFT)

        scrollbar = ttk.Scrollbar(self.overview_frame, command=self.overview.yview)
        scrollbar.pack(side=LEFT, fill="y")
        self.overview.configure(yscrollcommand=scrollbar.set)

    # Display receipt data in widgets
    def display_receipt_data(self, total_price, receipt_name, receipt_date):
        self.total_price_widget.configure(text=total_price)
        self.receipt_name_widget.configure(text=receipt_name)
        self.receipt_date_widget.configure(text=receipt_date)

    # Clear receipt data from widgets
    def clear_receipt_data(self):
        self.total_price_widget.configure(text="")
        self.receipt_name_widget.configure(text="")
        self.receipt_date_widget.configure(text="")

    # Adding items to treeview
    def add_items_to_treeview(self, items_df):
        for i, row in items_df.iterrows():
            self.overview.insert("", "end", text=i, values=list(row))

    # Clearing items in treeview
    def clear_treeview(self):
        items = self.overview.get_children()
        for item in items:
            self.overview.delete(item)

    # Updates list of user receipts
    def receipt_combobox_update(self, receipt_list):
        self.combobox_receipts.configure(values=receipt_list)
        self.combobox_var.set("")

    # Destroying receipts page
    def destroy_receipts_page_frame(self):
        self.receipts_frame.destroy()
