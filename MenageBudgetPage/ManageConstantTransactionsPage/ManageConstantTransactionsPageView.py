from tkinter import *
from tkinter import ttk


class ManageConstBudgetView:
    def __init__(self, master, controller, bg_color, incomes_df, expenses_df):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        self.incomes_df = incomes_df
        self.expenses_df = expenses_df

        # Define variables
        self.income_categories = ["salary", "added"]
        self.expenses_categories = ["rent", "bills", "groceries"]
        self.income_entry_var = StringVar()
        self.expense_entry_var = StringVar()
        self.income_category_var = StringVar()
        self.expense_category_var = StringVar()
        self.total_incomes = StringVar()
        self.total_expenses = StringVar()
        self.free_amount = StringVar()

        # Define default values for labels
        self.reset_labels()

        # Open budget frame
        self.menage_const_budget_frame = Frame(self.root, bg=self.bg_color)
        self.menage_const_budget_frame.grid()

        # Grid configuration in open budget frame
        self.menage_const_budget_frame.grid_columnconfigure(0, weight=0)

        # Income frame
        self.income_frame = Frame(self.menage_const_budget_frame, bg=self.bg_color)
        self.income_frame.grid(row=2, rowspan=6, column=1, sticky=W)

        # Expenses frame
        self.expenses_frame = Frame(self.menage_const_budget_frame, bg=self.bg_color)
        self.expenses_frame.grid(row=2, rowspan=6, column=2, sticky=E)

        # Labels and entries
        Label(self.menage_const_budget_frame, text="Edit your constant transactions", font=('Arial', 40),
              bg='light gray') \
            .grid(row=0, column=0, columnspan=4, sticky=EW, padx=140, pady=30, ipadx=135, ipady=50)

        Label(self.menage_const_budget_frame, textvariable=self.total_incomes, font=('Arial', 15), width=18,
              bg=self.bg_color) \
            .grid(row=8, column=1, sticky=W, pady=5)

        Label(self.menage_const_budget_frame, textvariable=self.total_expenses, font=('Arial', 15), width=18,
              bg=self.bg_color) \
            .grid(row=8, column=2, sticky=E, padx=15, pady=5)

        Label(self.menage_const_budget_frame, textvariable=self.free_amount, font=('Arial', 15), width=20,
              bg=self.bg_color) \
            .grid(row=9, column=1, columnspan=2, pady=10, sticky=W, padx=200)

        Label(self.menage_const_budget_frame, text="Category:", font=('Arial', 13), bg=self.bg_color) \
            .grid(row=2, column=0, sticky=W, padx=50)

        Label(self.menage_const_budget_frame, text="Category:", font=('Arial', 13), bg=self.bg_color) \
            .grid(row=2, column=3, sticky=W, padx=40)

        Label(self.menage_const_budget_frame, text="Amount:", font=('Arial', 13), bg=self.bg_color) \
            .grid(row=4, column=0, sticky=W, padx=50)
        Entry(self.menage_const_budget_frame, font=('Arial', 13), width=26, textvariable=self.income_entry_var) \
            .grid(row=5, column=0, sticky=W, padx=50)

        Label(self.menage_const_budget_frame, text="Amount:", font=('Arial', 13), bg=self.bg_color) \
            .grid(row=4, column=3, sticky=W, padx=40)
        Entry(self.menage_const_budget_frame, font=('Arial', 13), width=26, textvariable=self.expense_entry_var) \
            .grid(row=5, column=3, sticky=W, padx=40)

        # Combobox for category
        ttk.Combobox(self.menage_const_budget_frame, font=('Arial', 15), values=self.income_categories,
                     textvariable=self.income_category_var) \
            .grid(row=3, column=0, sticky=W, padx=50)

        ttk.Combobox(self.menage_const_budget_frame, font=('Arial', 15), values=self.expenses_categories,
                     textvariable=self.expense_category_var) \
            .grid(row=3, column=3, sticky=W, padx=40)

        # Add const income button
        Button(self.menage_const_budget_frame, text="Add income", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.add_income(
                   self.income_category_var.get(), self.income_entry_var.get()
               )) \
            .grid(row=6, column=0, sticky=W, padx=50)

        # Delete const income button
        Button(self.menage_const_budget_frame, text="Delete income", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.delete_income(
                   self.income_table.index(self.income_table.selection()[0])
               )) \
            .grid(row=7, column=0, sticky=W, padx=50)

        # Add const expanse button
        Button(self.menage_const_budget_frame, text="Add expanse", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.add_expense(
                   self.expense_category_var.get(), self.expense_entry_var.get()
               )) \
            .grid(row=6, column=3, sticky=W, padx=40)

        # Delete const expanse button
        Button(self.menage_const_budget_frame, text="Delete expanse", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.delete_expense(
                   self.expenses_table.index(self.expenses_table.selection()[0])
               )) \
            .grid(row=7, column=3, sticky=W, padx=40)

        # Update your const expanses
        Button(self.menage_const_budget_frame, text="Update your transactions", font=('Arial', 15), bg="light gray",
               width=20, command=lambda: self.controller.update_transactions()) \
            .grid(row=10, column=1, columnspan=2, sticky=W, padx=200, pady=10)

        # Back to manage budget page button
        Button(self.menage_const_budget_frame, text="back", font=('Arial', 15), bg='light gray', width=7,
               command=lambda: self.controller.back()) \
            .grid(row=11, column=0, columnspan=4, sticky=E, padx=20, pady=10)

        # Income treeview
        self.income_table = ttk.Treeview(self.income_frame, height=13)
        self.income_table["columns"] = list(self.incomes_df.columns)
        self.income_table.column("#0", width=50)

        for col in incomes_df.columns:
            self.income_table.column(col, width=75)

        self.income_table.heading("#0", text="Index", anchor="w")
        for col in incomes_df.columns:
            self.income_table.heading(col, text=col, anchor="w")
        self.income_table.pack(fill="both", expand=True, side=LEFT, anchor="w")

        income_scrollbar = ttk.Scrollbar(self.income_frame, command=self.income_table.yview)
        income_scrollbar.pack(side=LEFT, fill="y")
        self.income_table.configure(yscrollcommand=income_scrollbar.set)

        # Expenses treeview
        self.expenses_table = ttk.Treeview(self.expenses_frame, height=13)
        self.expenses_table["columns"] = list(self.expenses_df.columns)
        self.expenses_table.column("#0", width=50)

        for col in expenses_df.columns:
            self.expenses_table.column(col, width=75)

        self.expenses_table.heading("#0", text="Index", anchor="w")
        for col in expenses_df.columns:
            self.expenses_table.heading(col, text=col, anchor="w")
        self.expenses_table.pack(fill="both", expand=True, side=LEFT, anchor="w")

        expenses_scrollbar = ttk.Scrollbar(self.expenses_frame, command=self.expenses_table.yview)
        expenses_scrollbar.pack(side=LEFT, fill="y")
        self.expenses_table.configure(yscrollcommand=expenses_scrollbar.set)

    def add_items_to_incomes(self, incomes_df):
        for i, row, in incomes_df.iterrows():
            self.income_table.insert("", "end", text=i, values=list(row))

    def add_items_to_expenses(self, expenses_df):
        for i, row, in expenses_df.iterrows():
            self.expenses_table.insert("", "end", text=i, values=list(row))

    def clear_incomes(self):
        items = self.income_table.get_children()
        for item in items:
            self.income_table.delete(item)

    def clear_expenses(self):
        items = self.expenses_table.get_children()
        for item in items:
            self.expenses_table.delete(item)

    def update_labels(self, total_incomes, total_expenses, free_amount):
        self.total_incomes.set(f"Incomes: {total_incomes}")
        self.total_expenses.set(f"Expenses: {total_expenses}")
        self.free_amount.set(f"Free: {free_amount}")

    def reset_labels(self):
        self.total_incomes.set("Incomes: 0")
        self.total_expenses.set("Expenses: 0")
        self.free_amount.set("Free: 0")

    def destroy_budget_frame(self):
        self.menage_const_budget_frame.destroy()
