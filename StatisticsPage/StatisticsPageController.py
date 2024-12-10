from tkinter import messagebox
from StatisticsPage.StatisticsPageModel import StatisticsPageModel
from StatisticsPage.StatisticsPageView import StatisticsPageView


class StatisticPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.statistics_page_model = StatisticsPageModel()
        self.statistics_page_view = StatisticsPageView(self.root, self, self.bg_color)

    def submit_stat(self, time_period, stat_type):
        print(time_period)
        if not time_period == "All time":
            self.months = self.statistics_page_model.get_list_of_months(self.statistics_page_model.get_time_period_in_int(time_period))
        else:
            self.months = self.statistics_page_model.get_current_month()

        if stat_type == "General stats":
            months_info = self.statistics_page_model.get_budget_month_info(self.user_data, self.months[-1])
            expenses_categories = self.statistics_page_model.get_categories_for_expenses(self.user_data)
            incomes_categories = self.statistics_page_model.get_categories_for_incomes(self.user_data)

            combined_values = self.statistics_page_model.add_all_values(months_info)

            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.general_stats_overview(combined_values[1], combined_values[0], combined_values[2], incomes_categories, expenses_categories)
        elif stat_type == "Avg month stats":
            incomes, expenses, free_amount = self.statistics_page_model.sort_data(
                self.statistics_page_model.values_from_db(self.user_data, self.months[-1])
            )

            avg_spent = self.statistics_page_model.calculate_avg_value(incomes)
            avg_earned = self.statistics_page_model.calculate_avg_value(expenses)
            avg_free_amount = self.statistics_page_model.calculate_avg_value(free_amount)

            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.avg_month_stats_overview(avg_spent, avg_earned, avg_free_amount)
        elif stat_type == "Percent stats":
            combined_incomes = self.statistics_page_model.combine_dicts(
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="Income"),
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="ConstIncome")
            )
            sum_incomes = self.statistics_page_model.calculate_sum_of_values(list(combined_incomes.values()))

            combined_expenses = self.statistics_page_model.combine_dicts(
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="Expense"),
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="ConstExpense")
            )
            sum_expenses = self.statistics_page_model.calculate_sum_of_values(list(combined_expenses.values()))

            incomes = self.statistics_page_model.calculate_percent_value(combined_incomes, sum_incomes)
            expenses = self.statistics_page_model.calculate_percent_value(combined_expenses, sum_expenses)

            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.percent_stats_overview(incomes, expenses)
        elif stat_type == "The biggest incomes and expenses":
            combined_incomes = self.statistics_page_model.combine_dicts(
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="Income"),
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="ConstIncome")
            )
            max_income_category, max_income_value = self.statistics_page_model.max_value_from_dict(combined_incomes)

            combined_expenses = self.statistics_page_model.combine_dicts(
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="Expense"),
                self.statistics_page_model.get_cat_and_amount(self.user_data, self.months[-1], type_info="ConstExpense")
            )
            max_expenses_category, max_expenses_value = self.statistics_page_model.max_value_from_dict(combined_expenses)

            month_info_dict = self.statistics_page_model.month_info(self.user_data, self.months[-1])

            max_income_month, max_income = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="max", value_type=0)  # 0 is for income
            min_income_month, min_income = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="min", value_type=0)  # 0 is for income

            max_expense_month, max_expense = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="max", value_type=1)  # 1 is for expense
            min_expense_month, min_expense = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="min", value_type=1)  # 1 is for expense

            max_free_amount_month, max_free_amount = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="max", value_type=2)  # 2 is for free_amount
            min_free_amount_month, min_free_amount = self.statistics_page_model.operation_from_dict(
                month_info_dict, operation="min", value_type=2)  # 2 is for free_amount



            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.biggest_incomes_expenses_overview()
        elif stat_type == "Month budget stats":
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.month_budget_stats_overview()
        elif stat_type == "Incomes and expenses depending on the month":
            # circle graph of incomes and expenses by 12 months in year
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.incomes_expanses_on_month_overview()

    def back(self):
        self.statistics_page_view.destroy_statistics_frame()

    '''
    General stats
    '''

    def submit_category(self, type, category):
        result = self.statistics_page_model.calculate_sum_of_values(self.statistics_page_model.get_values_from_database(self.user_data, type, category, self.months[-1]))
        self.statistics_page_view.display_result(result, type, category)
