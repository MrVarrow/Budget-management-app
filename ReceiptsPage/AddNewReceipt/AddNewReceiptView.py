from tkinter import *
from tkinter import ttk
from pandastable import Table, TableModel
import pandas as pd

class AddNewReceiptView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Add new receipt frame
        self.add_new_receipt_frame = Frame(self.root)
        self.add_new_receipt_frame.grid(row=0, column=0)

        # Items frame
        self.items_frame = Frame(self.add_new_receipt_frame)
        self.items_frame.grid(row=1, rowspan=6, column=1)

        # Labels and entries
        Label(self.add_new_receipt_frame, text="Add new Receipt") \
            .grid(row=0, column=0, columnspan=3)

        Label(self.add_new_receipt_frame, text="Enter product name:") \
            .grid(row=1, column=0)
        Entry(self.add_new_receipt_frame) \
            .grid(row=2, column=0)

        Label(self.add_new_receipt_frame, text="Enter product price:") \
            .grid(row=3, column=0)
        Entry(self.add_new_receipt_frame) \
            .grid(row=4, column=0)

        Label(self.add_new_receipt_frame, text="Try by uploading a photo:\n"
                                               "Choose photo:") \
            .grid(row=1, column=2)

        # Submit item button
        Button(self.add_new_receipt_frame, text="Submit") \
            .grid(row=5, column=0)

        # Delete item button
        Button(self.add_new_receipt_frame, text="Delete") \
            .grid(row=6, column=0)

        # Add receipt button
        Button(self.add_new_receipt_frame, text="Add receipt") \
            .grid(row=7, column=1)

        # Choose path to receipt photo button
        Button(self.add_new_receipt_frame, text="path to selected file") \
            .grid(row=2, column=2)

        # Submit photo button
        Button(self.add_new_receipt_frame, text="Submit") \
            .grid(row=3, column=2)

        # Back to Receipt page
        Button(self.add_new_receipt_frame, text="Back") \
            .grid(row=7, column=2)

        data = {'Name': ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Lily', 'Mike', 'Emily'],
        'Age': [25, 30, 35, 40, 45, 50, 55, 60],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Moscow', 'Seoul']}
        df = pd.DataFrame(data)

        # Table for items
        table = ttk.Treeview(self.items_frame, height=3)
        table["columns"] = list(df.columns)
        table.column("#0", width=100)
        table.pack(fill="both", expand=True)
        for col in df.columns:
            table.column(col, width=100)
        table.pack(side=LEFT, fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.items_frame, command=table.yview)
        scrollbar.pack(side=LEFT, fill="y")
        table.configure(yscrollcommand=scrollbar.set)
        for i, row in df.iterrows():
            table.insert("", "end", text=i, values=list(row))
