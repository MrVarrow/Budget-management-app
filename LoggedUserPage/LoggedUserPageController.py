from LoggedUserPage.LoggedUserPageView import LoggedUserPageView
from LoggedUserPage.LoggedUserPageModel import LoggedUserPageModel
from SettingsPage.SettingsPageController import SettingsPageController
from AccountPage.AccountPageController import AccountPageController
from RateAppWindow.RateAppWindowController import RateAppWindowController
from QuestionnaireWindow.QuestionnaireWindowController import QuestionnaireWindowController
from ReceiptsPage.ReceiptsPageController import ReceiptsPageController
from ShoppingListPage.ShoppingListController import ShoppingListController
from MenageBudgetPage.ManageBudgetPageController import ManageBudgetController
from SavingsPage.SavingsPageController import SavingsPageController
from StatisticsPage.StatisticsPageController import StatisticPageController
from tkinter import messagebox
from SendEmails import send_email_to_rate_the_app, send_email_with_reminder_to_set_budget


class LoggedUserPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.logged_user_page_view = LoggedUserPageView(self.root, self, self.bg_color)
        self.logged_user_page_model = LoggedUserPageModel()

        today = self.logged_user_page_model.get_today_date()
        last_login = self.logged_user_page_model.get_last_login_date(self.user_data)
        goals_list = self.logged_user_page_model.get_user_goals_list(self.user_data)
        count = self.logged_user_page_model.count_1st_days_between_months(last_login, today)

        # Adds auto deposit amount to savings goal if needed
        if not count == 0:
            values_to_insert = self.logged_user_page_model.prepare_data(
                self.logged_user_page_model.get_const_transactions_info(self.user_data),
                self.logged_user_page_model.get_month_values(count))
            self.logged_user_page_model.save_const_transactions(values_to_insert)

            for goal in goals_list:
                goal_info = self.logged_user_page_model.get_info_about_goal(self.user_data, goal[0])
                progress = goal_info[4]
                auto_depo = goal_info[5]
                if not auto_depo == 0:
                    new_progress = self.logged_user_page_model.count_amount_added_to_goal(progress, auto_depo, count)
                    self.logged_user_page_model.update_amount_in_goal(new_progress, self.user_data, goal[0])

        # Update last seen date
        self.logged_user_page_model.update_last_seen(self.user_data, today)
        if not self.logged_user_page_model.check_if_user_rated(self.user_data) and self.user_data[3] == "1":
            send_email_to_rate_the_app(self.user_data[1], self.user_data[0])
        if self.user_data[3] == "1" and self.logged_user_page_model.is_day_25_or_later():
            send_email_with_reminder_to_set_budget(self.user_data[1], self.user_data[0])

    # Go into settings
    def settings(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        SettingsPageController(self.root, self.user_data, self.bg_color)

    # Go into user account
    def your_acc(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        AccountPageController(self.root, self.user_data, self.bg_color)

    # Go into manage budget page
    def manage_budget(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ManageBudgetController(self.root, self.user_data, self.bg_color)

    # Go into statistics page
    def stats(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        StatisticPageController(self.root, self.user_data, self.bg_color)

    # Go into shopping list page
    def shopping_list(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ShoppingListController(self.root, self.user_data, self.bg_color)

    # Go into savings page
    def savings(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        SavingsPageController(self.root, self.user_data, self.bg_color)

    # Go into receipts page
    def receipts(self):
        self.logged_user_page_view.destroy_logged_user_frame()
        ReceiptsPageController(self.root, self.user_data, self.bg_color)

    # Go into rate us window
    def rate_us(self):
        RateAppWindowController(self.root, self.user_data, self.bg_color)

    # Go into questionnaire window
    def questionnaire(self):
        QuestionnaireWindowController(self.root, self.user_data, self.bg_color)

    # Display question if user wants to log out, then takes action based on decision
    def logout(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to logout from Budget manager?")
        if result == "yes":
            self.logged_user_page_view.destroy_logged_user_frame()
            from UserLoginPage.UserLoginController import UserLoginController
            UserLoginController(self.root, self.bg_color)
        elif result == "no":
            pass

    # Display question if user wants to exit, then takes action based on decision
    def exit(self):
        result = messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass
