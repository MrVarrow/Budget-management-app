from tkinter import messagebox
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageModel import AdjustBudgetModel
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageView import AdjustBudgetView


class AdjustBudgetController:
    def __init__(self, root, user_data, bg_color, month_date):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.month_date = month_date

        self.total_expenses = 0
        self.total_incomes = 0
        self.free_amount = 0

        self.adjust_budget_model = AdjustBudgetModel()

        existing_budget = self.adjust_budget_model.get_budget_from_db(self.user_data, self.month_date)
        if existing_budget is None:
            self.incomes_df, self.expenses_df = self.adjust_budget_model.create_df()
        else:
            self.incomes_df, self.expenses_df = self.adjust_budget_model.budget_into_df(existing_budget)

        self.adjust_budget_view = AdjustBudgetView(
            self.root, self, self.bg_color, self.incomes_df, self.expenses_df, self.month_date
        )

        existing_const_budget = self.adjust_budget_model.get_const_from_db(self.user_data)
        if existing_const_budget is None:
            self.const_incomes_df, self.const_expenses_df = self.adjust_budget_model.create_df()
        else:
            self.const_incomes_df, self.const_expenses_df = self.adjust_budget_model.const_budget_into_df(
                existing_const_budget)
            self.adjust_budget_view.load_const_incomes(self.const_incomes_df)
            self.adjust_budget_view.load_const_expenses(self.const_expenses_df)

        self.combined_incomes_df = self.adjust_budget_model.add_dfs(self.const_incomes_df, self.incomes_df)
        self.combined_expenses_df = self.adjust_budget_model.add_dfs(self.const_expenses_df, self.expenses_df)

        self.const_expenses_len = len(self.const_expenses_df)
        self.const_incomes_len = len(self.const_incomes_df)

        self.total_incomes = self.adjust_budget_model.calculate_total_incomes(self.combined_incomes_df)
        self.total_expenses = self.adjust_budget_model.calculate_total_expenses(self.combined_expenses_df)
        self.free_amount = self.adjust_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.adjust_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.adjust_budget_view.clear_incomes()
        self.adjust_budget_view.clear_expenses()
        self.adjust_budget_view.add_items_to_incomes(self.combined_incomes_df, self.const_incomes_len)
        self.adjust_budget_view.add_items_to_expenses(self.combined_expenses_df, self.const_expenses_len)

    def add_income(self, category, amount):
        if self.adjust_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not self.adjust_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return
        self.incomes_df = self.adjust_budget_model.add_items_to_incomes(category, amount, self.incomes_df)
        self.combined_incomes_df = self.adjust_budget_model.add_dfs(self.const_incomes_df, self.incomes_df)
        self.total_incomes = self.adjust_budget_model.calculate_total_incomes(self.combined_incomes_df)
        self.free_amount = self.adjust_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.adjust_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.adjust_budget_view.clear_incomes()
        self.adjust_budget_view.add_items_to_incomes(self.combined_incomes_df, self.const_incomes_len)

    def delete_income(self, index):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your"
                                                       " budget incomes?")
            if result == "yes":
                self.incomes_df = self.adjust_budget_model.delete_from_incomes_df(index, self.incomes_df, combined=False)
                self.combined_incomes_df = self.adjust_budget_model.delete_from_incomes_df(index, self.combined_incomes_df, combined=True)
                self.total_incomes = self.adjust_budget_model.calculate_total_incomes(self.combined_incomes_df)
                self.free_amount = self.adjust_budget_model.calculate_free_amount(self.total_incomes,
                                                                                  self.total_expenses)

                self.adjust_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
                self.adjust_budget_view.clear_incomes()
                self.adjust_budget_view.add_items_to_incomes(self.combined_incomes_df, self.const_incomes_len)
        # fix to execute code after index error
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")
        except KeyError:
            messagebox.showinfo("Information", "You can't delete constant income")

    def add_expense(self, category, amount):
        if self.adjust_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not self.adjust_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return
        self.expenses_df = self.adjust_budget_model.add_items_to_expenses(category, amount, self.expenses_df)
        self.combined_expenses_df = self.adjust_budget_model.add_dfs(self.const_expenses_df, self.expenses_df)
        self.total_expenses = self.adjust_budget_model.calculate_total_expenses(self.combined_expenses_df)
        self.free_amount = self.adjust_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.adjust_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.adjust_budget_view.clear_expenses()
        self.adjust_budget_view.add_items_to_expenses(self.combined_expenses_df, self.const_expenses_len)

    def delete_expense(self, index):
        try:
            result = messagebox.askquestion("Warning", "Do you want to delete selected item from your"
                                                       " budget expenses?")
            if result == "yes":
                self.expenses_df = self.adjust_budget_model.delete_from_expenses_df(index, self.expenses_df, combined=False)
                self.combined_expenses_df = self.adjust_budget_model.delete_from_expenses_df(index, self.combined_expenses_df, combined=True)
                self.total_expenses = self.adjust_budget_model.calculate_total_expenses(self.combined_expenses_df)
                self.free_amount = self.adjust_budget_model.calculate_free_amount(self.total_incomes,
                                                                                  self.total_expenses)

                self.adjust_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
                self.adjust_budget_view.clear_expenses()
                self.adjust_budget_view.add_items_to_expenses(self.combined_expenses_df, self.const_expenses_len)
        except IndexError:
            messagebox.showinfo("Information", "Please select item to delete first, by clicking on it.")
        except KeyError:
            messagebox.showinfo("Information", "You can't delete constant expense")

    def update_budget(self):
        if not self.adjust_budget_model.check_if_budget_exists(self.user_data):
            self.adjust_budget_model.insert_budget(
                self.user_data, self.total_incomes, self.total_expenses, self.free_amount, self.month_date
            )
        else:
            self.adjust_budget_model.update_budget(
                self.month_date, self.total_incomes, self.total_expenses, self.free_amount
            )
            self.adjust_budget_model.delete_items_from_database(self.user_data)

        self.adjust_budget_model.insert_items_to_database(self.user_data, self.incomes_df, self.expenses_df, self.month_date)

        messagebox.showinfo("Information", "Your transactions has been updated successfully!")

    def back(self):
        from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
        self.adjust_budget_view.destroy_budget_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)

