from tkinter import *
from tkinter import ttk


class ShoppingListView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.combobox_var = StringVar()

        # Shopping list frame
        self.shopping_list_frame = Frame(self.root, bg=self.bg_color)
        self.shopping_list_frame.grid(row=0, column=0)

        # Item list frame
        self.list_items_frame = Frame(self.shopping_list_frame, bg=self.bg_color, borderwidth=2, relief="solid")
        self.list_items_frame.grid(row=1, rowspan=5, column=0, columnspan=2, sticky=E, padx=200, ipadx=180, ipady=170)

        Label(self.list_items_frame, text="HSVDVUSDYVU").grid()

        # Labels
        Label(self.shopping_list_frame, text="Your shopping lists", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=220, pady=40, ipadx=210, ipady=50)

        # Choosing receipts combobox
        ttk.Combobox(self.shopping_list_frame, font=('Arial', 20), textvariable=self.combobox_var, width=20) \
            .grid(row=1, column=0, sticky=W, padx=100, pady=40)

        # Open shopping list button
        Button(self.shopping_list_frame, text="Open shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.open_shopping_list()) \
            .grid(row=2, column=0, sticky=W, padx=100)

        # Edit shopping list button
        Button(self.shopping_list_frame, text="Edit shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.edit_shopping_list()) \
            .grid(row=3, column=0, sticky=W, padx=100, pady=20)

        # Delete shopping list button
        Button(self.shopping_list_frame, text="Delete shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.delete_shopping_list()) \
            .grid(row=4, column=0, sticky=W, padx=100, pady=20)

        # Add new shopping list button
        Button(self.shopping_list_frame, text="Add new shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.add_new_shopping_list()) \
            .grid(row=5, column=0, sticky=W, padx=100)

        # Back to logged user page button
        Button(self.shopping_list_frame, text="Back", font=('Arial', 15), bg='light gray', width=10,
               command=lambda: self.controller.back_to_logged_usr_page()) \
            .grid(row=6, column=0, columnspan=2, sticky=E, padx=50)

    def destroy_shopping_list_frame(self):
        self.shopping_list_frame.destroy()
