from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageModel import OpenBudgetModel
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageView import OpenBudgetView


class OpenBudgetController:
    def __init__(self, root, user_data, bg_color, month_date):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.month_date = month_date

        self.total_expenses = 0
        self.total_incomes = 0
        self.free_amount = 0

        self.open_budget_model = OpenBudgetModel()

        existing_budget = self.open_budget_model.get_budget_from_db(self.user_data, self.month_date)
        if existing_budget is None:
            self.incomes_df, self.expenses_df = self.open_budget_model.create_df()
        else:
            self.incomes_df, self.expenses_df = self.open_budget_model.budget_into_df(existing_budget)

        self.open_budget_view = OpenBudgetView(
            self.root, self, self.bg_color, self.incomes_df, self.expenses_df, self.month_date
        )

        existing_const_budget = self.open_budget_model.get_const_from_db(self.user_data)
        if existing_const_budget is None:
            self.const_incomes_df, self.const_expenses_df = self.open_budget_model.create_df()
        else:
            self.const_incomes_df, self.const_expenses_df = self.open_budget_model.const_budget_into_df(
                existing_const_budget)
            self.open_budget_view.load_const_incomes(self.const_incomes_df)
            self.open_budget_view.load_const_expenses(self.const_expenses_df)

        self.combined_incomes_df = self.open_budget_model.add_dfs(self.const_incomes_df, self.incomes_df)
        self.combined_expenses_df = self.open_budget_model.add_dfs(self.const_expenses_df, self.expenses_df)

        self.const_expenses_len = len(self.const_expenses_df)
        self.const_incomes_len = len(self.const_incomes_df)

        self.total_incomes = self.open_budget_model.calculate_total_incomes(self.combined_incomes_df)
        self.total_expenses = self.open_budget_model.calculate_total_expenses(self.combined_expenses_df)
        self.free_amount = self.open_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        self.open_budget_view.update_labels(self.total_incomes, self.total_expenses, self.free_amount)
        self.open_budget_view.clear_incomes()
        self.open_budget_view.clear_expenses()
        self.open_budget_view.add_items_to_incomes(self.combined_incomes_df, self.const_incomes_len)
        self.open_budget_view.add_items_to_expenses(self.combined_expenses_df, self.const_expenses_len)

    def back(self):
        from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
        self.open_budget_view.destroy_budget_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)
