from tkinter import *
from tkinter import ttk


class AddNewShoppingListView:
    def __init__(self, master, controller, bg_color, shopping_list_name, state):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        self.item_name = StringVar()
        self.item_price = StringVar()
        self.receipt_name = StringVar()

        # Add new receipt frame
        self.add_new_shopping_list_frame = Frame(self.root, bg=self.bg_color)
        self.add_new_shopping_list_frame.grid(row=0, column=0)

        # Items frame
        self.items_frame = Frame(self.add_new_shopping_list_frame, bg=self.bg_color)
        self.items_frame.grid(row=1, rowspan=6, column=1)

        # Labels and entries
        Label(self.add_new_shopping_list_frame, text="Add new shopping list", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=180, pady=40, ipadx=210, ipady=50)

        Label(self.add_new_shopping_list_frame, text="Enter product name:", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50)
        self.product_name_entry = Entry(self.add_new_shopping_list_frame, font=('Arial', 20), textvariable=self.item_name)
        self.product_name_entry.bind("<Button-1>", lambda e: self.product_name_entry.delete(0, END))
        self.item_name.set("ex. Tomato")
        self.product_name_entry.grid(row=2, column=0, sticky=W, padx=50)

        Label(self.add_new_shopping_list_frame, text="Enter quantity:", font=('Arial', 15)) \
            .grid(row=3, column=0, sticky=W, padx=50)
        self.product_quantity_entry = Entry(self.add_new_shopping_list_frame, font=('Arial', 20), textvariable=self.item_price)
        self.product_quantity_entry.bind("<Button-1>", lambda e: self.product_quantity_entry.delete(0, END))
        self.item_price.set("ex. 3")
        self.product_quantity_entry.grid(row=4, column=0, sticky=W, padx=50)


        self.shopping_list_name_entry = Entry(self.add_new_shopping_list_frame, textvariable=self.receipt_name, font=('Arial', 20))
        self.shopping_list_name_entry.bind("<Button-1>", lambda e: self.shopping_list_name_entry.delete(0, END))
        if shopping_list_name is None:
            self.receipt_name.set("Your shopping list name")
        else:
            self.receipt_name.set(shopping_list_name)
            self.shopping_list_name_entry.configure(state="disabled")
        self.shopping_list_name_entry.grid(row=7, column=1, pady=10)

        # Submit item button
        Button(self.add_new_shopping_list_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.submit_item(self.item_name.get(), self.item_price.get())) \
            .grid(row=5, column=0, sticky=W, padx=120, pady=5)

        # Delete item button (to delete it would take index of item)
        Button(self.add_new_shopping_list_frame, text="Delete", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.delete_item(self.table.item(self.table.selection()[0], 'values')[0])) \
            .grid(row=7, column=0, sticky=W, padx=120, pady=10)

        if state == "ADD":
            # Add receipt button
            Button(self.add_new_shopping_list_frame, text="Add shopping list", font=('Arial', 20), bg="light gray", width=15,
                   command=lambda: self.controller.add_receipt(self.receipt_name.get())) \
                .grid(row=8, column=1)

        elif state == "UPDATE":
            # Update receipt button
            Button(self.add_new_shopping_list_frame, text="Update shopping list", font=('Arial', 20), bg="light gray", width=15,
                   command=lambda: self.controller.update_receipt()) \
                .grid(row=8, column=1)

        # Edit element button
        Button(self.add_new_shopping_list_frame, text="Edit element", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.edit_element(self.table.item(self.table.selection()[0], 'values'))) \
            .grid(row=6, column=0, sticky=W, padx=120, pady=10)

        # Back to Receipt page
        Button(self.add_new_shopping_list_frame, text="Back", font=('Arial', 15), bg="light gray", width=7,
               command=lambda: self.controller.back_to_receipt_page()) \
            .grid(row=8, column=2, sticky=E, padx=20)

        # Clear all button
        Button(self.add_new_shopping_list_frame, text="Clear List", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.clear_receipt_data()) \
            .grid(row=8, column=0, sticky=W, padx=120, pady=5)

    # Edit element window
    def edit_element_window(self, product_name, product_price):
        name = StringVar()
        price = StringVar()

        self.edit_window = Toplevel(self.root, bg=self.bg_color)
        self.edit_window.geometry("400x200")
        self.edit_window.title("Editing element")
        self.edit_window.resizable(False, False)

        Label(self.edit_window, text="Edit element", bg="light gray", font=('Arial', 20)) \
            .grid(row=0, column=0, pady=5, sticky=W, padx=92, ipadx=32)

        Label(self.edit_window, text="New name:", font=('Arial', 12)) \
            .grid(row=1, column=0, sticky=W, padx=90)
        prodduct_name_widget = Entry(self.edit_window, textvariable=name, font=('Arial', 15))
        name.set(product_name)
        prodduct_name_widget.grid(row=2, column=0, sticky=W, padx=90)

        Label(self.edit_window, text="New price:", font=('Arial', 12)) \
            .grid(row=3, column=0, sticky=W, padx=90)
        product_price_widget = Entry(self.edit_window, textvariable=price, font=('Arial', 15))
        price.set(product_price)
        product_price_widget.grid(row=4, column=0, sticky=W, padx=90)

        Button(self.edit_window, text="Apply", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.apply_edit(product_name, name.get(), price.get())) \
            .grid(row=5, column=0, sticky=W, padx=20, pady=5)
        Button(self.edit_window, text="Close", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.discard_edit()) \
            .grid(row=5, column=0, sticky=W, padx=260, pady=5)

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