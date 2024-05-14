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
