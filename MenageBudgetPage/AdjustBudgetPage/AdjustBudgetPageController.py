from tkinter import messagebox
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageModel import AdjustBudgetModel
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageView import AdjustBudgetView


class AdjustBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.adjust_budget_model = AdjustBudgetModel()
        self.adjust_budget_view = AdjustBudgetView(self.root, self, self.bg_color)

    def add_const_income(self):
        ...

    def delete_const_income(self):
        ...

    def add_const_expense(self):
        ...

    def delete_const_expense(self):
        ...

    def update_const_transactions(self):
        ...

    def back(self):
        from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
        self.adjust_budget_view.destroy_budget_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)

