from tkinter import messagebox
from MenageBudgetPage.ManageBudgetPageModel import ManageBudgetModel
from MenageBudgetPage.ManageBudgetPageView import ManageBudgetView
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageController import OpenBudgetController


class ManageBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        # ...
        self.manage_budget_model = ManageBudgetModel()
        self.manage_budget_view = ManageBudgetView(self.root, self, self.bg_color,
                                                   self.manage_budget_model.get_12_months()
                                                   )

    def open_budget(self):
        self.manage_budget_view.destroy_manage_budget_frame()
        OpenBudgetController(self.root, self, self.bg_color)

    def edit_budget(self):
        ...

    def manage_constants(self):
        ...

    def delete_budget(self):
        ...

    def choosing_month(self):
        ...

