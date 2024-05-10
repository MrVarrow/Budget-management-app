from tkinter import *
from tkinter import ttk

# FIX THE VIEW OF OVERVIEW
class ShoppingListView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.combobox_var = StringVar()
        self.check_vars = []

        # Shopping list frame
        self.shopping_list_frame = Frame(self.root, bg=self.bg_color)
        self.shopping_list_frame.grid(row=0, column=0)

        # Item list frame
        self.list_items_frame = Frame(self.shopping_list_frame, bg=self.bg_color, borderwidth=2, relief="solid", width=600, height=400)
        self.list_items_frame.grid(row=1, rowspan=5, column=0, columnspan=2, sticky=E, padx=200)

        # Labels
        Label(self.shopping_list_frame, text="Your shopping lists", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=220, pady=40, ipadx=210, ipady=50)

        # Choosing receipts combobox
        self.combobox_shopping_lists = ttk.Combobox(self.shopping_list_frame, font=('Arial', 20), textvariable=self.combobox_var, width=20)
        self.combobox_shopping_lists.grid(row=1, column=0, sticky=W, padx=100, pady=40)

        # Open shopping list button
        Button(self.shopping_list_frame, text="Open shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.open_shopping_list(self.combobox_var.get())) \
            .grid(row=2, column=0, sticky=W, padx=100)

        # Edit shopping list button
        Button(self.shopping_list_frame, text="Edit shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.edit_shopping_list(self.combobox_var.get())) \
            .grid(row=3, column=0, sticky=W, padx=100, pady=20)

        # Delete shopping list button
        Button(self.shopping_list_frame, text="Delete shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.delete_shopping_list(self.combobox_var.get())) \
            .grid(row=4, column=0, sticky=W, padx=100, pady=20)

        # Add new shopping list button
        Button(self.shopping_list_frame, text="Add new shopping list", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.add_new_shopping_list()) \
            .grid(row=5, column=0, sticky=W, padx=100)

        # Back to logged user page button
        Button(self.shopping_list_frame, text="Back", font=('Arial', 15), bg='light gray', width=10,
               command=lambda: self.controller.back_to_logged_usr_page()) \
            .grid(row=6, column=0, columnspan=2, sticky=E, padx=50)

    # Updates list of user receipts
    def shopping_lists_combobox_update(self, shopping_lists):
        self.combobox_shopping_lists.configure(values=shopping_lists)
        self.combobox_var.set("")

    # Destroys shopping list frame
    def destroy_shopping_list_frame(self):
        self.shopping_list_frame.destroy()

    # Creates overview of shopping list
    def create_overview(self, shopping_list_name, items_df, shopping_list_date):
        canvas = Canvas(self.list_items_frame, width=600, height=400)
        canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas to hold the labels
        labels_frame = ttk.Frame(canvas)

        # Add the labels frame to the canvas
        canvas.create_window((0, 0), window=labels_frame, anchor="nw")

        # Create heading label
        Label(labels_frame, text=f"Shopping list name: {shopping_list_name}, Creation date: {shopping_list_date}", font=('Arial', 15)).pack(pady=5)

        # Create the labels inside the labels_frame
        for index, row in items_df.iterrows():
            item_name = row['Item name']
            item_quantity = row['Item quantity']
            check_var = BooleanVar()
            self.check_vars.append(check_var.get())
            item_checkbutton = Checkbutton(labels_frame, text=f"{item_name}, Quantity {item_quantity}", font=('Arial', 13),
                        bg="light gray", width=63, anchor="w", variable=check_var,
                        command=lambda i=index: self.controller.check_box(i, self.check_vars))
            item_checkbutton.pack(pady=10, anchor="w")

        # Button for checking if list is complete
        Button(labels_frame, text="Done", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.check_list(shopping_list_name)) \
            .pack()

        # Add a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self.list_items_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Bind the labels frame to detect when it is resized
        labels_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Bind the mousewheel event to the canvas and labels_frame
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mousewheel)
        labels_frame.bind_all("<MouseWheel>", on_mousewheel)
