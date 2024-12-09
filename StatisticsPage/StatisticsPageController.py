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



            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.percent_stats_overview()
        elif stat_type == "The biggest incomes and expenses":
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.biggest_incomes_expenses_overview()
        elif stat_type == "Month budget stats":
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.month_budget_stats_overview()
        elif stat_type == "Incomes and expenses depending on the month":
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
