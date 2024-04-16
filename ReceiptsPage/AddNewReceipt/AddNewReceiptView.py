from tkinter import *
from tkinter import ttk
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
        Label(self.add_new_receipt_frame, text="Add new Receipt", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)

        Label(self.add_new_receipt_frame, text="Enter product name:", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50)
        Entry(self.add_new_receipt_frame, font=('Arial', 20)) \
            .grid(row=2, column=0, sticky=W, padx=50)

        Label(self.add_new_receipt_frame, text="Enter product price:", font=('Arial', 15)) \
            .grid(row=3, column=0, sticky=W, padx=50)
        Entry(self.add_new_receipt_frame, font=('Arial', 20)) \
            .grid(row=4, column=0, sticky=W, padx=50)

        Label(self.add_new_receipt_frame, font=('Arial', 15), text="Try by uploading a photo:\n"
                                               "Choose photo:") \
            .grid(row=1, column=2, sticky=E, padx=65)

        # Submit item button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10) \
            .grid(row=5, column=0, sticky=W, padx=120, pady=20)

        # Delete item button
        Button(self.add_new_receipt_frame, text="Delete", font=('Arial', 20), bg="light gray", width=10) \
            .grid(row=6, column=0, sticky=W, padx=120, pady=20)

        # Add receipt button
        Button(self.add_new_receipt_frame, text="Add receipt", font=('Arial', 20), bg="light gray", width=10) \
            .grid(row=7, column=1, pady=10)

        # Choose path to receipt photo button
        Button(self.add_new_receipt_frame, text="path to selected file", font=('Arial', 20), bg="light gray") \
            .grid(row=2, rowspan=2, column=2, sticky=SE, padx=50)

        # Submit photo button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10) \
            .grid(row=4, rowspan=2, column=2, sticky=SE, padx=100)

        # Back to Receipt page
        Button(self.add_new_receipt_frame, text="Back", font=('Arial', 15), bg="light gray", width=7) \
            .grid(row=8, column=2, sticky=E)

        data = {'Name': ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Lily', 'Mike', 'Emily'],
        'Age': [25, 30, 35, 40, 45, 50, 55, 60],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Moscow', 'Seoul']}
        df = pd.DataFrame(data)

        # Table for items
        table = ttk.Treeview(self.items_frame, height=15)
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


