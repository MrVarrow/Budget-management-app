from tkinter import messagebox
from SavingsPage.SavingsPageView import SavingsPageView
from SavingsPage.SavingsPageModel import SavingsPageModel
from MenageBudgetPage.ManageConstantTransactionsPage.ManageConstantTransactionsPageModel import ManageConstBudgetModel
from MenageBudgetPage.AdjustBudgetPage.AdjustBudgetPageModel import AdjustBudgetModel
from MenageBudgetPage.ManageBudgetPageModel import ManageBudgetModel
from MenageBudgetPage.OpenBudgetPage.OpenBudgetPageModel import OpenBudgetModel
from Validations.Validations import correct_price_format, string_has_int_format, variable_is_none


class SavingsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.savings_page_model = SavingsPageModel()

        self.savings_page_view = SavingsPageView(
            self.root, self, self.bg_color, self.savings_page_model.get_user_goals(self.user_data)
        )

        self.manage_const_budget_model = ManageConstBudgetModel()
        self.manage_budget_model = ManageBudgetModel()
        self.adjust_budget_model = AdjustBudgetModel()
        self.open_budget_model = OpenBudgetModel()

        self.total_expenses = 0
        self.total_incomes = 0
        self.free_amount = 0

        self.goal_info = None


    def submit_open_goal(self, goal_name):
        self.goal_info = self.savings_page_model.get_info_about_goal(self.user_data, goal_name)
        time_left = self.savings_page_model.calculate_time_left_for_goal(self.goal_info[3])
        progress = self.savings_page_model.calculate_percent_of_goal_accomplished(self.goal_info[2], self.goal_info[4])
        # fill the overview
        self.savings_page_view.destroy_overview_frame()
        self.savings_page_view.open_goal_overview(self.goal_info, time_left, progress)

    def delete_goal(self, goal_name):
        result = messagebox.askquestion(title='Warning', message="Do you want to delete this goal?")
        if result == "yes":
            self.savings_page_model.delete_goal_from_database(self.user_data, goal_name)

            self.savings_page_view.destroy_overview_frame()
            self.savings_page_view.overview_frame_creation()
            self.savings_page_view.initial_overview()
            self.savings_page_view.update_goal_list(self.savings_page_model.get_user_goals(self.user_data))
        elif result == "no":
            pass


    def make_new_goal(self):
        self.savings_page_view.make_new_goal_window()

    def bank_deposit(self):
        self.profit_df = None
        self.money_deposit_df = None
        self.savings_page_view.destroy_overview_frame()
        self.savings_page_view.bank_deposit_overview()

    def investments(self):
        self.profit_df = None
        self.money_deposit_df = None
        self.savings_page_view.destroy_overview_frame()
        self.savings_page_view.investments_overview()


    def back(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        self.savings_page_view.destroy_savings_frame()
        LoggedUserPageController(self.root, self.user_data, self.bg_color)

    # Make new goal window buttons
    def submit_goal(self, goal_name, goal_amount, goal_date):
        if not self.savings_page_model.goal_name_validation(goal_name):
            messagebox.showinfo("Information", "Wrong name.")
            return

        if not self.savings_page_model.goal_amount_validation(goal_amount):
            messagebox.showinfo("Information", "Wrong amount.")
            return

        if not self.savings_page_model.goal_date_validation(goal_date):
            messagebox.showinfo("Information", "Wrong date, please select future date.")
            return

        self.savings_page_model.save_goal_to_database(self.user_data, goal_name, goal_amount, goal_date, progress=0, automatic_deposit=0)
        self.savings_page_view.destroy_make_goal_window()
        messagebox.showinfo("Information", "Your goal has been successfully added!")

    # Goal Overview buttons
    def deposit(self):
        self.savings_page_view.deposit_window()

    def withdraw(self):
        self.savings_page_view.withdraw_window()

    def save_auto_deposit(self, goal_name, automatic_deposit, goal_amount):
        if not self.savings_page_model.goal_amount_validation(automatic_deposit) \
                or not self.savings_page_model.goal_amount_deposit_validation(automatic_deposit, goal_amount,
                                                                              self.savings_page_model.get_progress_from_database(self.user_data, goal_name)):
            messagebox.showinfo("Information", "Wrong amount.")
            return


        self.savings_page_model.update_automatic_deposit_in_database(self.user_data, goal_name, automatic_deposit)
        # auto depo to const
        if not self.savings_page_model.check_if_deposit_exists(self.user_data, goal_name):
            self.savings_page_model.insert_automatic_deposit_to_constants(self.user_data, goal_name, automatic_deposit)
        else:
            self.savings_page_model.update_automatic_deposit_to_constants(int(automatic_deposit), goal_name, self.user_data)
        self.savings_page_view.update_auto_deposit_label(automatic_deposit)

        # get totals
        existing_budget = self.manage_const_budget_model.get_budget_from_db(self.user_data)
        if existing_budget is None:
            self.incomes_df, self.expenses_df = self.manage_const_budget_model.create_df()
        else:
            self.incomes_df, self.expenses_df = self.manage_const_budget_model.get_budget_info_df(existing_budget)

        self.total_incomes = self.manage_const_budget_model.calculate_total_incomes(self.incomes_df)
        self.total_expenses = self.manage_const_budget_model.calculate_total_expenses(self.expenses_df)
        self.free_amount = self.manage_const_budget_model.calculate_free_amount(self.total_incomes, self.total_expenses)

        # const budget change
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

        messagebox.showinfo("Information", "Auto Deposit Successfully Changed.")
    # Deposit submit button

    def submit_deposit(self, deposit_amount, goal_name, goal_amount):
        if not self.savings_page_model.goal_amount_validation(deposit_amount) \
                or not self.savings_page_model.goal_amount_deposit_validation(deposit_amount, goal_amount,
                                                                              self.savings_page_model.get_progress_from_database(self.user_data, goal_name)):
            messagebox.showinfo("Information", "Wrong amount.")
            return

        new_progress = self.savings_page_model.deposit_to_progress(
            self.savings_page_model.get_progress_from_database(self.user_data, goal_name), int(deposit_amount)
        )
        self.savings_page_model.update_progress_in_database(self.user_data, goal_name, new_progress)
        self.savings_page_view.update_progress(self.savings_page_model.calculate_percent_of_goal_accomplished(goal_amount, new_progress), self.savings_page_model.get_info_about_goal(self.user_data, goal_name))
        self.savings_page_view.destroy_deposit_window()

        messagebox.showinfo("Information", "Added deposit to goal.")

    # Withdraw submit button
    def submit_withdraw(self, withdraw_amount, goal_name, goal_amount):
        if not self.savings_page_model.goal_amount_validation(withdraw_amount) \
                or not self.savings_page_model.goal_amount_withdraw_validation(withdraw_amount, self.savings_page_model.get_progress_from_database(self.user_data, goal_name)):
            messagebox.showinfo("Information", "Wrong amount.")
            return

        new_progress = self.savings_page_model.withdraw_from_progress(
            self.savings_page_model.get_progress_from_database(self.user_data, goal_name), int(withdraw_amount)
        )
        self.savings_page_model.update_progress_in_database(self.user_data, goal_name, new_progress)
        self.savings_page_view.update_progress(self.savings_page_model.calculate_percent_of_goal_accomplished(goal_amount, new_progress), self.savings_page_model.get_info_about_goal(self.user_data, goal_name))
        self.savings_page_view.destroy_withdraw_window()

        messagebox.showinfo("Information", "Withdrawn deposit from goal.")


    def confirm_calculate_investments(self, entry_payment: str, future_payments: str, frequency_of_payments: str, investing_time: str,
                               rate_of_return: str):
        # Add inputs validations
        if not correct_price_format(entry_payment):
            messagebox.showinfo("Information", "Entry payment has Wrong value")
            return

        if not correct_price_format(future_payments):
            messagebox.showinfo("Information", "Future payments has Wrong Value")
            return

        if not string_has_int_format(investing_time):
            messagebox.showinfo("Information", "Value of investing time has to be natural number.")
            return

        if not correct_price_format(rate_of_return) or not 0 < int(rate_of_return) <= 20:
            messagebox.showinfo("Information", "Value rate of return has to be maximum 20%")
            return


        list_of_values, list_of_years, list_of_money_deposited = self.savings_page_model.investments_calculator(
            float(entry_payment), float(future_payments), int(frequency_of_payments), int(investing_time),
            float(self.savings_page_model.convert_percent_to_float(int(rate_of_return)))
        )
        self.profit_df = self.savings_page_model.create_profit_dataframe(list_of_years, list_of_values)
        self.money_deposit_df = self.savings_page_model.create_profit_dataframe(list_of_years, list_of_money_deposited)


        self.savings_page_view.update_total_value_label(self.savings_page_model.get_total_investments_value(list_of_values))

    def confirm_calculate_bank_deposit(self, amount, bank_deposit_time, interest_rate, capitalization_time):
        if not correct_price_format(amount):
            messagebox.showinfo("Information", "Amount has Wrong value")
            return

        if not string_has_int_format(bank_deposit_time):
            messagebox.showinfo("Information", "Value of bank deposit time has to be natural number.")
            return

        if not correct_price_format(interest_rate) or not 0 < int(interest_rate) <= 20:
            messagebox.showinfo("Information", "Value rate of return has to be maximum 20%")
            return

        if capitalization_time == "1" or capitalization_time == "12" or capitalization_time == "4":
            list_of_values, list_of_years, list_of_money_deposited =\
                self.savings_page_model.bank_deposit_calculator_capitalization(
                    float(amount), int(bank_deposit_time), float(self.savings_page_model.convert_percent_to_float(int(interest_rate))),
                    int(capitalization_time)
                )
        else:
            list_of_values, list_of_years, list_of_money_deposited =\
                self.savings_page_model.bank_deposit_calculator_no_capitalization(
                    float(amount), int(bank_deposit_time), float(self.savings_page_model.convert_percent_to_float(int(interest_rate)))
                )
        self.profit_df = self.savings_page_model.create_profit_dataframe(list_of_years, list_of_values)
        self.money_deposit_df = self.savings_page_model.create_profit_dataframe(list_of_years, list_of_money_deposited)

        self.savings_page_view.update_total_value_label(
            self.savings_page_model.get_total_investments_value(list_of_values))

    def create_table(self):
        if variable_is_none(self.profit_df):
            messagebox.showinfo("Information", "You have to make calculations to see a table")
        self.savings_page_view.create_table(self.profit_df)

    def create_graph(self):
        if variable_is_none(self.profit_df) or variable_is_none(self.money_deposit_df):
            messagebox.showinfo("Information", "You have to make calculations to see a graph")

        self.savings_page_view.create_graph(self.savings_page_model.create_plot_dataframe_investments(self.profit_df, self.money_deposit_df))
