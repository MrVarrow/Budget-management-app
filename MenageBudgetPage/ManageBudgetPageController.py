from tkinter import messagebox
from MenageBudgetPage.ManageBudgetPageModel import ManageBudgetModel
from MenageBudgetPage.ManageBudgetPageView import ManageBudgetView
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageController import OpenBudgetController
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageController import AdjustBudgetController
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageController import\
    ManageConstBudgetController


class ManageBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.month_date = ""

        self.manage_budget_model = ManageBudgetModel()
        self.manage_budget_view = ManageBudgetView(self.root, self, self.bg_color,
                                                   self.manage_budget_model.get_12_months()
                                                   )

    def open_budget(self):
        if not self.month_date == "":
            self.manage_budget_view.destroy_manage_budget_frame()
            OpenBudgetController(self.root, self.user_data, self.bg_color, self.month_date)
            return
        messagebox.showinfo("Information", "You have to select month first")

    def edit_budget(self):
        if not self.month_date == "":
            self.manage_budget_view.destroy_manage_budget_frame()
            AdjustBudgetController(self.root, self.user_data, self.bg_color, self.month_date)
            return
        messagebox.showinfo("Information", "You have to select month first")

    def manage_constants(self):
        self.manage_budget_view.destroy_manage_budget_frame()
        ManageConstBudgetController(self.root, self.user_data, self.bg_color)

    def delete_budget(self):
        result = messagebox.askquestion("Warning", "Do you want to delete budget for selected month?")
        if result == "yes":
            if not self.month_date == "":
                self.manage_budget_model.delete_budget_transactions(self.user_data, self.month_date)
                self.manage_budget_model.delete_budget_month(self.user_data, self.month_date)
                self.manage_budget_view.clear_info_about_month()
                self.month_date = ""
                return
            messagebox.showinfo("Information", "You have to select month first")
        messagebox.showinfo("Information", "Budget deleted successfully.")

    def back(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        self.manage_budget_view.destroy_manage_budget_frame()
        LoggedUserPageController(self.root, self.user_data, self.bg_color)

    def choosing_month(self, date: str):
        self.month_date = date
        self.manage_budget_view.show_chosen_date(date)
        self.manage_budget_view.clear_info_about_month()
        incomes, expenses, free_amount = self.manage_budget_model.get_info_about_budget(self.user_data[0], date)
        c_incomes, c_expenses, c_free_amount = self.manage_budget_model.get_info_about_const_budget(self.user_data)
        if incomes is None:
            sum_incomes, sum_expenses, sum_free_amount = c_incomes, c_expenses, c_free_amount
        else:
            sum_incomes, sum_expenses, sum_free_amount = incomes, expenses, free_amount

        self.manage_budget_view.show_info_about_budget(sum_incomes, sum_expenses, sum_free_amount)
