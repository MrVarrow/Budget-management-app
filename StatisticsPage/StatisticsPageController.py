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
        ...

    def back(self):
        self.statistics_page_view.destroy_statistics_frame()
