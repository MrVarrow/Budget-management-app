from tkinter import *
from tkinter import ttk


class AddNewReceiptView:
    def __init__(self, master, controller, bg_color, receipt_name, state):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        # Entries variables
        self.item_name = StringVar()
        self.item_price = StringVar()
        self.receipt_name = StringVar()

        # File path variable
        self.filepath = StringVar()
        self.filepath.set("None")

        # Add new receipt frame
        self.add_new_receipt_frame = Frame(self.root, bg=self.bg_color)
        self.add_new_receipt_frame.grid(row=0, column=0)

        # Items frame
        self.items_frame = Frame(self.add_new_receipt_frame, bg=self.bg_color)
        self.items_frame.grid(row=1, rowspan=6, column=1)

        # Labels and entries
        Label(self.add_new_receipt_frame, text="Add new Receipt", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)

        Label(self.add_new_receipt_frame, text="Enter product name:", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50)
        self.product_name_entry = Entry(self.add_new_receipt_frame, font=('Arial', 20), textvariable=self.item_name)
        self.product_name_entry.bind("<Button-1>", lambda e: self.product_name_entry.delete(0, END))
        self.item_name.set("ex. Tomato")
        self.product_name_entry.grid(row=2, column=0, sticky=W, padx=50)

        Label(self.add_new_receipt_frame, text="Enter product price:", font=('Arial', 15)) \
            .grid(row=3, column=0, sticky=W, padx=50)
        self.product_price_entry = Entry(self.add_new_receipt_frame, font=('Arial', 20), textvariable=self.item_price)
        self.product_price_entry.bind("<Button-1>", lambda e: self.product_price_entry.delete(0, END))
        self.item_price.set("ex. 12.50")
        self.product_price_entry.grid(row=4, column=0, sticky=W, padx=50)
        Label(self.add_new_receipt_frame, font=('Arial', 15), text="Try by uploading a photo:\n"
                                                                   "Choose photo:") \
            .grid(row=1, column=2, sticky=E, padx=70)

        self.receipt_name_entry = Entry(self.add_new_receipt_frame, textvariable=self.receipt_name, font=('Arial', 20))
        self.receipt_name_entry.bind("<Button-1>", lambda e: self.receipt_name_entry.delete(0, END))
        if receipt_name is None:
            self.receipt_name.set("Your receipt name")
        else:
            self.receipt_name.set(receipt_name)
            self.receipt_name_entry.configure(state="disabled")
        self.receipt_name_entry.grid(row=7, column=1, pady=10)

        # Submit item button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.submit_item(self.item_name.get(), self.item_price.get())) \
            .grid(row=5, column=0, sticky=W, padx=120, pady=20)

        # Delete item button (to delete it would take index of item)
        Button(self.add_new_receipt_frame, text="Delete", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.delete_item(self.table.item(self.table.selection()[0], 'values')[0])) \
            .grid(row=6, column=0, sticky=W, padx=120, pady=20)

        if state == "ADD":
            # Add receipt button
            Button(self.add_new_receipt_frame, text="Add receipt", font=('Arial', 20), bg="light gray", width=15,
                   command=lambda: controller.add_receipt(self.receipt_name.get())) \
                .grid(row=8, column=1)

        elif state == "UPDATE":
            # Update receipt button
            Button(self.add_new_receipt_frame, text="Update receipt", font=('Arial', 20), bg="light gray", width=15,
                   command=lambda: controller.update_receipt()) \
                .grid(row=8, column=1)

        # Choose path to receipt photo button
        Button(self.add_new_receipt_frame, textvariable=self.filepath, font=('Arial', 12), height=3, width=30,
               wraplength=250, bg="light gray", command=lambda: controller.choose_path_to_photo()) \
            .grid(row=2, rowspan=2, column=2, sticky=SE, padx=50)

        # Submit photo button
        Button(self.add_new_receipt_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.submit_photo(self.filepath.get())) \
            .grid(row=4, rowspan=2, column=2, sticky=SE, padx=100)

        # Edit element button
        Button(self.add_new_receipt_frame, text="Edit element", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.edit_element(self.table.item(self.table.selection()[0], 'values'))) \
            .grid()

        # Back to Receipt page
        Button(self.add_new_receipt_frame, text="Back", font=('Arial', 15), bg="light gray", width=7,
               command=lambda: controller.back_to_receipt_page()) \
            .grid(row=8, column=2, sticky=E)

        # Clear all button
        Button(self.add_new_receipt_frame, text="Clear Receipt", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: controller.clear_receipt_data()) \
            .grid(row=7, column=0, sticky=W, padx=120)

    # Edit element window
    def edit_element_window(self, product_name, product_price):
        name = StringVar()
        price = StringVar()

        self.edit_window = Toplevel(self.root, bg=self.bg_color)
        self.edit_window.geometry("400x200")
        self.edit_window.title("Editing element")
        self.edit_window.resizable(False, False)

        Label(self.edit_window, text="Edit element") \
            .grid()

        prodduct_name_widget = Entry(self.edit_window, textvariable=name)
        name.set(product_name)
        prodduct_name_widget.grid()

        product_price_widget = Entry(self.edit_window, textvariable=price)
        price.set(product_price)
        product_price_widget.grid()

        Button(self.edit_window, text="Apply", command=lambda: self.controller.apply_edit(name.get(), price.get())) \
            .grid()
        Button(self.edit_window, text="Close", command=lambda: self.controller.discard_edit()) \
            .grid()

    # Destroying edit element window
    def edit_element_widnow_destroy(self):
        self.edit_window.destroy()


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

    # Display path to photo on button
    def configure_file_path_view(self, filepath):
        self.filepath.set(filepath)

    # Resets all after adding receipt
    def reset_receipt(self):
        self.receipt_name_entry.delete(0, END)
        self.product_name_entry.delete(0, END)
        self.product_price_entry.delete(0, END)
        self.item_name.set("ex. Tomato")
        self.item_price.set("ex. 12.50")
        self.receipt_name.set("Your receipt name")
        self.clear_treeview()
        self.filepath.set("None")

    # Clear treeview
    def clear_treeview(self):
        for item in self.table.get_children():
            self.table.delete(item)





