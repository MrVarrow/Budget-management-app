from tkinter import messagebox
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageModel import ManageConstBudgetModel
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageView import ManageConstBudgetView
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageModel import AdjustBudgetModel
from MenageBudgetPage.ManageBudgetPageModel import ManageBudgetModel
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageModel import OpenBudgetModel
from Validations.Validations import correct_price_format, empty_string_inside_widget


class ManageConstBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.total_expenses = 0
        self.total_incomes = 0
        self.free_amount = 0

        self.manage_budget_model = ManageBudgetModel()
        self.adjust_budget_model = AdjustBudgetModel()
        self.open_budget_model = OpenBudgetModel()

        self.manage_const_budget_model = ManageConstBudgetModel()

        existing_budget = self.manage_const_budget_model.get_budget_from_db(self.user_data)
        if existing_budget is None:
            self.incomes_df, self.expenses_df = self.manage_const_budget_model.create_df()
        else:
            self.incomes_df, self.expenses_df = self.manage_const_budget_model.get_budget_info_df(existing_budget)
        self.manage_const_budget_view = ManageConstBudgetView(
            self.root, self, self.bg_color, self.incomes_df, self.expenses_df
        )

        self.total_incomes = self.manage_const_budget_model.calculate_total_incomes(self.incomes_df)
        self.total_expenses = self.manage_const_budget_model.calculate_total_expenses(self.expenses_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.manage_const_budget_view.clear_incomes()
        self.manage_const_budget_view.clear_expenses()
        self.manage_const_budget_view.add_items_to_incomes(self.incomes_df)
        self.manage_const_budget_view.add_items_to_expenses(self.expenses_df)

    def add_income(self, category: str, amount: str):
        if empty_string_inside_widget(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not correct_price_format(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return

        self.incomes_df = self.manage_const_budget_model.add_items_to_incomes(category, amount, self.incomes_df)
        self.total_incomes = self.manage_const_budget_model.calculate_total_incomes(self.incomes_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.manage_const_budget_view.clear_incomes()
        self.manage_const_budget_view.add_items_to_incomes(self.incomes_df)

    def delete_income(self, index: int):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your"
                                                       " constant incomes?")
            if result == "yes":
                self.incomes_df = self.manage_const_budget_model.delete_from_incomes_df(index, self.incomes_df)
                self.total_incomes = self.manage_const_budget_model.calculate_total_incomes(self.incomes_df)
                self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes,
                                                                                        self.total_expenses)

                self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
                self.manage_const_budget_view.clear_incomes()
                self.manage_const_budget_view.add_items_to_incomes(self.incomes_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")

    def add_expense(self, category: str, amount: str):
        if empty_string_inside_widget(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not correct_price_format(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return
        self.expenses_df = self.manage_const_budget_model.add_items_to_expenses(category, amount, self.expenses_df)
        self.total_expenses = self.manage_const_budget_model.calculate_total_expenses(self.expenses_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.manage_const_budget_view.clear_expenses()
        self.manage_const_budget_view.add_items_to_expenses(self.expenses_df)

    def delete_expense(self, index: int):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your"
                                                       " constant expenses?")
            if result == "yes":
                self.expenses_df = self.manage_const_budget_model.delete_from_expenses_df(index, self.expenses_df)
                self.total_expenses = self.manage_const_budget_model.calculate_total_expenses(self.expenses_df)
                self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes,
                                                                                        self.total_expenses)

                self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
                self.manage_const_budget_view.clear_expenses()
                self.manage_const_budget_view.add_items_to_expenses(self.expenses_df)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")

    def update_transactions(self):
        if not self.manage_const_budget_model.check_if_budget_exists(self.user_data):
            self.manage_const_budget_model.insert_budget(
                self.user_data, self.total_incomes, self.total_expenses, self.free_amount
            )
        else:
            self.manage_const_budget_model.update_const_budget(
                self.user_data, self.total_incomes, self.total_expenses, self.free_amount
            )
            self.manage_const_budget_model.delete_items_from_database(self.user_data)
        self.manage_const_budget_model.insert_items_to_database(self.user_data, self.incomes_df, self.expenses_df)
        self.incomes_df, self.expenses_df = self.manage_const_budget_model.create_df()

        # update future month budgets

        months = self.manage_budget_model.get_12_months()
        for month in months:
            if self.adjust_budget_model.check_if_budget_exists(month):
                budget = self.open_budget_model.get_budget_from_db(self.user_data, month)
                c_incomes_df, c_expenses_df = self.open_budget_model.budget_into_df(budget)
                combined_incomes_df = self.open_budget_model.add_dfs(c_incomes_df, self.incomes_df)
                combined_expenses_df = self.open_budget_model.add_dfs(c_expenses_df, self.expenses_df)

                total_incomes = self.open_budget_model.calculate_total_incomes(combined_incomes_df)
                total_expenses = self.open_budget_model.calculate_total_expenses(combined_expenses_df)
                free_amount = self.open_budget_model.calculate_free_amount(total_incomes, total_expenses)

                self.adjust_budget_model.update_budget(month, total_incomes, total_expenses, free_amount)

        self.manage_const_budget_view.reset_labels()
        self.manage_const_budget_view.clear_expenses()
        self.manage_const_budget_view.clear_incomes()
        messagebox.showinfo("Information", "Your transactions has been updated successfully!")

    def back(self):
        from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
        self.manage_const_budget_view.destroy_budget_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)
