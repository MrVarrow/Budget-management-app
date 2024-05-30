from tkinter import messagebox
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageModel import ManageConstBudgetModel
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageView import ManageConstBudgetView


# errors of not selecting dont works
class ManageConstBudgetController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.total_expenses = 0
        self.total_incomes = 0
        self.free_amount = 0

        self.manage_const_budget_model = ManageConstBudgetModel()
        self.incomes_df, self.expenses_df = self.manage_const_budget_model.create_df()
        self.manage_const_budget_view = ManageConstBudgetView(
            self.root, self, self.bg_color, self.incomes_df, self.expenses_df
        )

    def add_income(self, category, amount):
        if self.manage_const_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not self.manage_const_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return

        self.incomes_df = self.manage_const_budget_model.add_items_to_incomes(category, amount, self.incomes_df)
        self.total_incomes = self.manage_const_budget_model.calculate_total_incomes(self.incomes_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.manage_const_budget_view.clear_incomes()
        self.manage_const_budget_view.add_items_to_incomes(self.incomes_df)

    def delete_income(self, index):
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

    def add_expense(self, category, amount):
        if self.manage_const_budget_model.check_category(category):
            messagebox.showinfo("Information", "You have to select category first.")
            return
        if not self.manage_const_budget_model.check_amount(amount):
            messagebox.showinfo("Information", "Entered amount is incorrect or contains not allowed characters "
                                               "please follow format: xx.xx or xx")
            return
        self.expenses_df = self.manage_const_budget_model.add_items_to_expenses(category, amount, self.expenses_df)
        self.total_expenses = self.manage_const_budget_model.calculate_total_expenses(self.expenses_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.manage_const_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.manage_const_budget_view.clear_expenses()
        self.manage_const_budget_view.add_items_to_expenses(self.expenses_df)

    def delete_expense(self, index):
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
            self.manage_const_budget_model.update_budget(
                self.user_data, self.total_incomes, self.total_expenses, self.free_amount
            )
            self.manage_const_budget_model.delete_items_from_database(self.user_data)
        self.manage_const_budget_model.insert_items_to_database(self.user_data, self.incomes_df, self.expenses_df)
        self.incomes_df, self.expenses_df = self.manage_const_budget_model.create_df()

        self.manage_const_budget_view.reset_labels()
        self.manage_const_budget_view.clear_expenses()
        self.manage_const_budget_view.clear_incomes()
        messagebox.showinfo("Information", "Your transactions has been updated successfully!")

    def back(self):
        from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
        self.manage_const_budget_view.destroy_budget_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)
