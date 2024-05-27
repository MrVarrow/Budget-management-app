from tkinter import messagebox
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageModel import ManageConstBudgetModel
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageView import ManageConstBudgetView


class ManageConstBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.manage_const_budget_model = ManageConstBudgetModel()
        self.manage_const_budget_view = ManageConstBudgetView(self.root, self, self.bg_color)

    def add_income(self, category, amount):
        if not self.manage_const_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
        if not self.manage_const_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")

    def delete_income(self):
        ...

    def add_expense(self, category, amount):
        if not self.manage_const_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
        if not self.manage_const_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")

    def delete_expense(self):
        ...

    def update_transactions(self):
        ...

    def back(self):
        ...
