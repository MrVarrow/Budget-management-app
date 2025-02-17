from tkinter import *


class ManageBudgetView:
    def __init__(self, master, controller, bg_color, months):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        self.months = months

        # Defining variables
        self.chosen_month = StringVar()
        self.month_budget_info = StringVar()

        # Frame creation
        self.manage_budget_frame = Frame(self.root, bg=self.bg_color)
        self.manage_budget_frame.grid(row=0, column=0)

        # Labels
        Label(self.manage_budget_frame, text="Manage your budget", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=6, sticky=EW, padx=190, pady=40, ipadx=215, ipady=50)

        self.chosen_month_label = Label(self.manage_budget_frame, text=self.chosen_month.get(),
                                        font=('Arial', 15), width=40, height=2)
        self.chosen_month_label.grid(row=3, column=2, columnspan=2)

        Label(self.manage_budget_frame, textvariable=self.month_budget_info, font=('Arial', 15), width=20,
              height=5, borderwidth=2, relief="solid") \
            .grid(row=4, rowspan=2, column=2, columnspan=2)

        # Month buttons
        for i in range(12):
            row = 2 if i >= 6 else 1
            col = i if i < 6 else i - 6
            month_button = Button(self.manage_budget_frame, text=self.months[i], font=('Arial', 15), bg='light gray',
                                  width=10, command=lambda date=self.months[i]: self.controller.choosing_month(date))
            month_button.grid(row=row, column=col, pady=10, ipady=5)

        # Open budget button
        Button(self.manage_budget_frame, text="Open budget", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.open_budget()) \
            .grid(row=4, column=0, columnspan=3, sticky=W, padx=100, pady=30)

        # Edit budget button
        Button(self.manage_budget_frame, text="Edit budget", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.edit_budget()) \
            .grid(row=5, column=0, columnspan=3, sticky=W, padx=100, pady=10)

        # Manage constant incomes and expenses button
        Button(self.manage_budget_frame, text="Manage constants", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.manage_constants()) \
            .grid(row=4, column=3, columnspan=3, sticky=E, padx=100, pady=30)

        # Delete budget button
        Button(self.manage_budget_frame, text="Delete budget", font=('Arial', 20), bg='light gray', width=20,
               command=lambda: self.controller.delete_budget()) \
            .grid(row=5, column=3, columnspan=3, sticky=E, padx=100, pady=10)

        # Back to logged user page button
        Button(self.manage_budget_frame, text="Back", font=('Arial', 15), bg='light gray', width=8,
               command=lambda: self.controller.back()) \
            .grid(row=6, column=0, columnspan=6, sticky=E, pady=40, padx=20)

        self.clear_info_about_month()

    def show_chosen_date(self, date: str):
        self.chosen_month.set(date)
        self.chosen_month_label.configure(text=self.chosen_month.get())

    def show_info_about_budget(self, incomes, expenses, free_amount):
        self.month_budget_info.set(f"Incomes: {incomes}\n"
                                   f"Expenses: {expenses}\n"
                                   f"Free amount: {free_amount}\n")

    def clear_info_about_month(self):
        self.month_budget_info.set(f"Incomes: \n"
                                   f"Expenses: \n"
                                   f"Free amount: \n")

    def destroy_manage_budget_frame(self):
        self.manage_budget_frame.destroy()
