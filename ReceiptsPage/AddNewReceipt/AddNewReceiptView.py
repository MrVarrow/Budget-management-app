from tkinter import *
from tkinter import ttk
import pandas as pd


class AddNewReceiptView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        # Entries variables
        self.item_name = StringVar()
        self.item_price = StringVar()

        # Add new receipt frame
        self.add_new_receipt_frame = Frame(self.root)
        self.add_new_receipt_frame.grid(row=0, column=0)

        # Items frame
        self.items_frame = Frame(self.add_new_receipt_frame)
        self.items_frame.grid(row=1, rowspan=6, column=1)

        # Labels and entries
        Label(self.add_new_receipt_frame, text="Add new Receipt", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)

        Label(self.add_new_receipt_frame, text="Enter product name:", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50)
        Entry(self.add_new_receipt_frame, font=('Arial', 20), textvariable=self.item_name) \
            .grid(row=2, column=0, sticky=W, padx=50)

        Label(self.add_new_receipt_frame, text="Enter product price:", font=('Arial', 15)) \
            .grid(row=3, column=0, sticky=W, padx=50)
        Entry(self.add_new_receipt_frame, font=('Arial', 20), textvariable=self.item_price) \
            .grid(row=4, column=0, sticky=W, padx=50)

        Label(self.add_new_receipt_frame, font=('Arial', 15), text="Try by uploading a photo:\n"
                                               "Choose photo:") \
            .grid(row=1, column=2, sticky=E, padx=65)

        # Submit item button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.submit_item(self.item_name.get(), self.item_price.get())) \
            .grid(row=5, column=0, sticky=W, padx=120, pady=20)

        # Delete item button (to delete it would take index of item)
        Button(self.add_new_receipt_frame, text="Delete", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.delete_item(self.table.selection())) \
            .grid(row=6, column=0, sticky=W, padx=120, pady=20)

        # Add receipt button
        Button(self.add_new_receipt_frame, text="Add receipt", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.add_receipt()) \
            .grid(row=7, column=1, pady=10)

        # Choose path to receipt photo button
        Button(self.add_new_receipt_frame, text="path to selected file", font=('Arial', 20), bg="light gray",
               command=lambda: controller.choose_path_to_photo()) \
            .grid(row=2, rowspan=2, column=2, sticky=SE, padx=50)

        # Submit photo button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.submit_photo()) \
            .grid(row=4, rowspan=2, column=2, sticky=SE, padx=100)

        # Back to Receipt page
        Button(self.add_new_receipt_frame, text="Back", font=('Arial', 15), bg="light gray", width=7,
               command=lambda: controller.back_to_receipt_page()) \
            .grid(row=8, column=2, sticky=E)

    # Creating treeview table and scrollbar
    def create_treeview(self, treeview_df):
        self.table = ttk.Treeview(self.items_frame, height=15)
        self.table["columns"] = list(treeview_df.columns)
        self.table.column("#0", width=50)

        for col in treeview_df.columns:
            self.table.column(col, width=100)

        self.table.heading("#0", text="Index", anchor="w")
        for col in treeview_df.columns:
            self.table.heading(col, text=col, anchor="w")

        self.table.pack(fill="both", expand=True, side=LEFT)

        scrollbar = ttk.Scrollbar(self.items_frame, command=self.table.yview)
        scrollbar.pack(side=LEFT, fill="y")
        self.table.configure(yscrollcommand=scrollbar.set)

    # Update values in treeview
    def update_treeview(self, updated_df):
        for i, row in updated_df.iterrows():
            self.table.insert("", "end", text=i, values=list(row))

    # Deleting old values in treeview
    def delete_items_in_treeview(self):
        items = self.table.get_children()
        for item in items:
            self.table.delete(item)

    def delete_item_from_treeview(self, selected_item):

        if selected_item:
            self.table.delete(selected_item)