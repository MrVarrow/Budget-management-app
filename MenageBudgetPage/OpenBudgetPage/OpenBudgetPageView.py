from tkinter import *
from tkinter import ttk


class OpenBudgetView:
    def __init__(self, master, controller, bg_color, incomes_df, expenses_df, month_date):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        self.month_date = month_date
        self.incomes_df = incomes_df
        self.expenses_df = expenses_df

        # Define variables
        self.total_incomes = StringVar()
        self.total_expenses = StringVar()
        self.free_amount = StringVar()

        # Define default values for labels
        self.reset_labels()

        # Open budget frame
        self.open_budget_frame = Frame(self.root, bg=self.bg_color)
        self.open_budget_frame.grid()

        # Income frame
        self.income_frame = Frame(self.open_budget_frame, bg=self.bg_color)
        self.income_frame.grid(row=2, column=0, columnspan=2, sticky=W, padx=370)

        # Expenses frame
        self.expenses_frame = Frame(self.open_budget_frame, bg=self.bg_color)
        self.expenses_frame.grid(row=2, column=1, sticky=W, padx=75)

        # Labels
        Label(self.open_budget_frame, text="Your monthly budget", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=190, pady=42, ipadx=210, ipady=50)

        Label(self.open_budget_frame, text=self.month_date, font=('Arial', 15), width=10, bg=self.bg_color) \
            .grid(row=1, column=0, columnspan=2, sticky=W, padx=600, pady=10)

        Label(self.open_budget_frame, textvariable=self.total_incomes, font=('Arial', 15), width=18, bg=self.bg_color) \
            .grid(row=3, column=0, sticky=E, padx=75, pady=10)

        Label(self.open_budget_frame, textvariable=self.total_expenses, font=('Arial', 15), width=18, bg=self.bg_color)\
            .grid(row=3, column=1, sticky=W, padx=75, pady=10)

        Label(self.open_budget_frame, textvariable=self.free_amount, font=('Arial', 15), width=20, bg=self.bg_color) \
            .grid(row=4, column=0, columnspan=2)

        # Back to manage budget page button
        Button(self.open_budget_frame, text="back", font=('Arial', 15), bg='light gray', width=7,
               command=lambda: self.controller.back()) \
            .grid(row=5, column=0, columnspan=2, sticky=E, padx=60, pady=10)

        # Income treeview
        self.income_table = ttk.Treeview(self.income_frame, height=13)
        self.income_table["columns"] = list(self.incomes_df.columns)
        self.income_table.column("#0", width=50)

        for col in incomes_df.columns:
            self.income_table.column(col, width=75)

        self.income_table.heading("#0", text="Index", anchor="w")
        for col in incomes_df.columns:
            self.income_table.heading(col, text=col, anchor="w")
        self.income_table.pack(fill="both", expand=True, side=LEFT, anchor="e")

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

    def add_items_to_incomes(self, incomes_df, length):
        self.income_table.tag_configure("const", background="light gray")
        for i, row, in incomes_df.iterrows():
            if i < length:
                tags = ("const",)
            else:
                tags = ()
            self.income_table.insert("", "end", text=i, values=list(row), tags=tags)

    def add_items_to_expenses(self, expenses_df, length):
        self.expenses_table.tag_configure("const", background="light gray")
        for i, row, in expenses_df.iterrows():
            if i < length:
                tags = ("const",)
            else:
                tags = ()
            self.expenses_table.insert("", "end", text=i, values=list(row), tags=tags)

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

    def load_const_incomes(self, const_incomes_df):
        self.income_table.tag_configure("const", background="light gray")
        for i, row, in const_incomes_df.iterrows():
            self.income_table.insert("", "end", text=i, values=list(row), tags=("const",))

    def load_const_expenses(self, const_expenses_df):
        self.expenses_table.tag_configure("const", background="light gray")
        for i, row, in const_expenses_df.iterrows():
            self.expenses_table.insert("", "end", text=i, values=list(row), tags=("const",))

    def reset_labels(self):
        self.total_incomes.set("Incomes: 0")
        self.total_expenses.set("Expenses: 0")
        self.free_amount.set("Free: 0")

    def destroy_budget_frame(self):
        self.open_budget_frame.destroy()
