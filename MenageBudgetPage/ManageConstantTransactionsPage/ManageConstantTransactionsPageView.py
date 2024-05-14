from tkinter import *
from tkinter import ttk


class ManageConstBudgetView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

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
        Label(self.open_budget_frame, text="Your constant transactions", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=150, pady=40, ipadx=210, ipady=50)

        Label(self.open_budget_frame, text="total income: ", font=('Arial', 15), bg="red", width=18) \
            .grid(row=3, column=0, sticky=E, padx=75, pady=10)

        Label(self.open_budget_frame, text="total expenses: ", font=('Arial', 15), bg="red", width=18) \
            .grid(row=3, column=1, sticky=W, padx=75, pady=10)

        Label(self.open_budget_frame, text="Free amount: ", font=('Arial', 15), bg="red", width=20) \
            .grid(row=4, column=0, columnspan=2)

        # Back to manage budget page button
        Button(self.open_budget_frame, text="back", font=('Arial', 15), bg='light gray', width=7,
               command=lambda: self.destroy_budget_frame()) \
            .grid(row=5, column=0, columnspan=2, sticky=E, padx=60, pady=10)

        # Income treeview
        self.income_table = ttk.Treeview(self.income_frame, height=13)
        self.income_table.pack(fill="both", expand=True, side=LEFT, anchor="e")

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
        self.open_budget_frame.destroy()
