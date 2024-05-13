from tkinter import messagebox
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageModel import OpenBudgetModel
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageView import OpenBudgetView


class OpenBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.open_budget_model = OpenBudgetModel()
        self.open_budget_view = OpenBudgetView(self.root, self, self.bg_color)

