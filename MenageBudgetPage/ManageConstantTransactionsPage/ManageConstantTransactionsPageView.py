from tkinter import *
from tkinter import ttk


class ManageConstBudgetView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.income_categories = []
        self.expenses_categories = []
        self.income_entry_var = StringVar()
        self.expense_entry_var = StringVar()

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
            .grid(row=0, column=0, columnspan=4, sticky=EW, padx=140, pady=20, ipadx=135, ipady=50)

        Label(self.menage_const_budget_frame, text="date", font=('Arial', 15), bg="red", width=10) \
            .grid(row=1, column=1, columnspan=2, pady=5, sticky=W, padx=250)

        Label(self.menage_const_budget_frame, text="total incomes: ", font=('Arial', 15), bg="red", width=18) \
            .grid(row=8, column=1, sticky=W, pady=5)

        Label(self.menage_const_budget_frame, text="total expenses: ", font=('Arial', 15), bg="red", width=18) \
            .grid(row=8, column=2, sticky=E, padx=15, pady=5)

        Label(self.menage_const_budget_frame, text="Free amount: ", font=('Arial', 15), bg="red", width=20) \
            .grid(row=9, column=1, columnspan=2, pady=10, sticky=W, padx=200)

        Label(self.menage_const_budget_frame, text="Category:", font=('Arial', 13)) \
            .grid(row=2, column=0, sticky=W, padx=50)

        Label(self.menage_const_budget_frame, text="Category:", font=('Arial', 13)) \
            .grid(row=2, column=3, sticky=W, padx=40)

        Label(self.menage_const_budget_frame, text="Amount:", font=('Arial', 13)) \
            .grid(row=4, column=0, sticky=W, padx=50)
        Entry(self.menage_const_budget_frame, font=('Arial', 13), width=26, textvariable=self.income_entry_var) \
            .grid(row=5, column=0, sticky=W, padx=50)

        Label(self.menage_const_budget_frame, text="Amount:", font=('Arial', 13)) \
            .grid(row=4, column=3, sticky=W, padx=40)
        Entry(self.menage_const_budget_frame, font=('Arial', 13), width=26, textvariable=self.expense_entry_var) \
            .grid(row=5, column=3, sticky=W, padx=40)

        # Combobox for category
        ttk.Combobox(self.menage_const_budget_frame, font=('Arial', 15), values=self.income_categories) \
            .grid(row=3, column=0, sticky=W, padx=50)

        ttk.Combobox(self.menage_const_budget_frame, font=('Arial', 15), values=self.expenses_categories) \
            .grid(row=3, column=3, sticky=W, padx=40)

        # Add const income button
        Button(self.menage_const_budget_frame, text="Add income", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.add_const_income()) \
            .grid(row=6, column=0, sticky=W, padx=50)

        # Delete const income button
        Button(self.menage_const_budget_frame, text="Delete income", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.delete_const_income()) \
            .grid(row=7, column=0, sticky=W, padx=50)

        # Add const expanse button
        Button(self.menage_const_budget_frame, text="Add expanse", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.add_const_expense()) \
            .grid(row=6, column=3, sticky=W, padx=40)

        # Delete const expanse button
        Button(self.menage_const_budget_frame, text="Delete expanse", font=('Arial', 15), bg="light gray", width=21,
               command=lambda: self.controller.delete_const_expense()) \
            .grid(row=7, column=3, sticky=W, padx=40)

        # Update your const expanses
        Button(self.menage_const_budget_frame, text="Update your transactions", font=('Arial', 15), bg="light gray",
               width=20, command=lambda: self.controller.update_const_transactions()) \
            .grid(row=10, column=1, columnspan=2, sticky=W, padx=200)

        # Back to manage budget page button
        Button(self.menage_const_budget_frame, text="back", font=('Arial', 15), bg='light gray', width=7,
               command=lambda: self.controller.back()) \
            .grid(row=11, column=0, columnspan=4, sticky=E, padx=20, pady=10)

        # Income treeview
        self.income_table = ttk.Treeview(self.income_frame, height=13)
        self.income_table.pack(fill="both", expand=True, side=LEFT, anchor="w")

        income_scrollbar = ttk.Scrollbar(self.income_frame, command=self.income_table.yview)
        income_scrollbar.pack(side=LEFT, fill="y")
        self.income_table.configure(yscrollcommand=income_scrollbar.set)

        # Expenses treeview
        self.expenses_table = ttk.Treeview(self.expenses_frame, height=13)
        self.expenses_table.pack(fill="both", expand=True, side=LEFT, anchor="w")

        expenses_scrollbar = ttk.Scrollbar(self.expenses_frame, command=self.expenses_table.yview)
        expenses_scrollbar.pack(side=LEFT, fill="y")
        self.expenses_table.configure(yscrollcommand=expenses_scrollbar.set)

    def destroy_budget_frame(self):
        self.menage_const_budget_frame.destroy()
