from tkinter import *
from tkinter import ttk


class AddNewShoppingListView:
    def __init__(self, master, controller, bg_color, shopping_list_name, state):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.item_name = StringVar()
        self.item_quantity = StringVar()
        self.shopping_list_name = StringVar()

        # Add new shopping list frame
        self.add_new_shopping_list_frame = Frame(self.root, bg=self.bg_color)
        self.add_new_shopping_list_frame.grid(row=0, column=0)

        # Items frame
        self.items_frame = Frame(self.add_new_shopping_list_frame, bg=self.bg_color)
        self.items_frame.grid(row=1, rowspan=6, column=1)

        # Labels and entries
        Label(self.add_new_shopping_list_frame, text="Add new shopping list", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=180, pady=43, ipadx=210, ipady=50)

        Label(self.add_new_shopping_list_frame, text="Enter product name:", font=('Arial', 15), bg=self.bg_color) \
            .grid(row=1, column=0, sticky=W, padx=50)
        self.product_name_entry = Entry(self.add_new_shopping_list_frame, font=('Arial', 20),
                                        textvariable=self.item_name)
        self.product_name_entry.bind("<Button-1>", lambda e: self.product_name_entry.delete(0, END))
        self.item_name.set("ex. Tomato")
        self.product_name_entry.grid(row=2, column=0, sticky=W, padx=50)

        Label(self.add_new_shopping_list_frame, text="Enter quantity:", font=('Arial', 15), bg=self.bg_color) \
            .grid(row=3, column=0, sticky=W, padx=50)
        self.product_quantity_entry = Entry(self.add_new_shopping_list_frame, font=('Arial', 20),
                                            textvariable=self.item_quantity)
        self.product_quantity_entry.bind("<Button-1>", lambda e: self.product_quantity_entry.delete(0, END))
        self.item_quantity.set("ex. 3")
        self.product_quantity_entry.grid(row=4, column=0, sticky=W, padx=50)

        self.shopping_list_name_entry = Entry(self.add_new_shopping_list_frame, textvariable=self.shopping_list_name,
                                              font=('Arial', 20))
        self.shopping_list_name_entry.bind("<Button-1>", lambda e: self.shopping_list_name_entry.delete(0, END))
        # If adding new: leave entry open for edit, if updating: disable editing and display name of shopping list
        if shopping_list_name is None:
            self.shopping_list_name.set("Your shopping list name")
        else:
            self.shopping_list_name.set(shopping_list_name)
            self.shopping_list_name_entry.configure(state="disabled")
        self.shopping_list_name_entry.grid(row=7, column=1, pady=10)

        # Submit item button
        Button(self.add_new_shopping_list_frame, text="Submit", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.submit_item(self.item_name.get(), self.item_quantity.get())) \
            .grid(row=5, column=0, sticky=W, padx=120, pady=5)

        # Delete item button (to delete it would take index of item)
        Button(self.add_new_shopping_list_frame, text="Delete", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.delete_item(self.table.selection())) \
            .grid(row=7, column=0, sticky=W, padx=120, pady=10)

        # Change type of button depending on state
        if state == "ADD":
            # Add shopping list button
            Button(self.add_new_shopping_list_frame, text="Add shopping list", font=('Arial', 20), bg="light gray",
                   width=15, command=lambda: self.controller.add_shopping_list(self.shopping_list_name.get())) \
                .grid(row=8, column=1)

        elif state == "UPDATE":
            # Update shopping list button
            Button(self.add_new_shopping_list_frame, text="Update shopping list", font=('Arial', 20), bg="light gray",
                   width=15, command=lambda: self.controller.update_shopping_list()) \
                .grid(row=8, column=1)

        # Edit element button
        Button(self.add_new_shopping_list_frame, text="Edit element", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.edit_element(self.table.selection())) \
            .grid(row=6, column=0, sticky=W, padx=120, pady=10)

        # Back to shopping list page
        Button(self.add_new_shopping_list_frame, text="Back", font=('Arial', 15), bg="light gray", width=7,
               command=lambda: self.controller.back_to_shopping_list_page()) \
            .grid(row=8, column=2, sticky=E, padx=20)

        # Clear all button
        Button(self.add_new_shopping_list_frame, text="Clear List", font=('Arial', 20), bg="light gray", width=10,
               command=lambda: self.controller.clear_shopping_list_list()) \
            .grid(row=8, column=0, sticky=W, padx=120, pady=5)

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

    # Resets all after adding shopping list
    def reset_shopping_list(self):
        self.product_name_entry.delete(0, END)
        self.product_name_entry.delete(0, END)
        self.product_quantity_entry.delete(0, END)
        self.item_name.set("ex. Tomato")
        self.item_quantity.set("ex. 3")
        self.shopping_list_name.set("Your shopping list name")
        self.clear_treeview()

    # Clear treeview
    def clear_treeview(self):
        for item in self.table.get_children():
            self.table.delete(item)

    '''
    Edit element window
    '''

    # Edit element window
    def edit_element_window(self, product_name: str, product_price: str):
        name = StringVar()
        quantity = StringVar()

        # New window popup creation
        self.edit_window = Toplevel(self.root, bg=self.bg_color)
        self.edit_window.geometry("400x200")
        self.edit_window.title("Editing element")
        self.edit_window.resizable(False, False)

        # Labels and entries
        Label(self.edit_window, text="Edit element", bg="light gray", font=('Arial', 20)) \
            .grid(row=0, column=0, pady=5, sticky=W, padx=92, ipadx=32)

        Label(self.edit_window, text="New name:", font=('Arial', 12)) \
            .grid(row=1, column=0, sticky=W, padx=90)
        product_name_widget = Entry(self.edit_window, textvariable=name, font=('Arial', 15))
        name.set(product_name)
        product_name_widget.grid(row=2, column=0, sticky=W, padx=90)

        Label(self.edit_window, text="New price:", font=('Arial', 12)) \
            .grid(row=3, column=0, sticky=W, padx=90)
        product_quantity_widget = Entry(self.edit_window, textvariable=quantity, font=('Arial', 15))
        quantity.set(product_price)
        product_quantity_widget.grid(row=4, column=0, sticky=W, padx=90)

        # Apply changes button
        Button(self.edit_window, text="Apply", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.apply_edit(product_name, name.get(), quantity.get())) \
            .grid(row=5, column=0, sticky=W, padx=20, pady=5)

        # Close button
        Button(self.edit_window, text="Close", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.discard_edit()) \
            .grid(row=5, column=0, sticky=W, padx=260, pady=5)

        self.edit_window.grab_set()

    # Destroying edit element window
    def edit_element_window_destroy(self):
        self.edit_window.destroy()
