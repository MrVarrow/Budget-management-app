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
            months = self.statistics_page_model.get_list_of_months(self.statistics_page_model.get_time_period_in_int(time_period))
        else:
            months = self.statistics_page_model.get_current_month()

        if stat_type == "General stats":
            months_info = self.statistics_page_model.get_budget_month_info(self.user_data, months[-1])
            self.statistics_page_model.add_all_values(months_info)
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.general_stats_overview()
        elif stat_type == "Avg month stats":
            self.statistics_page_view.destroy_overview_frame()
            self.statistics_page_view.avg_month_stats_overview()
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
