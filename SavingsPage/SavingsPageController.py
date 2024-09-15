from tkinter import messagebox
from SavingsPage.SavingsPageView import SavingsPageView
from SavingsPage.SavingsPageModel import SavingsPageModel


class SavingsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.savings_page_model = SavingsPageModel()

        self.savings_page_view = SavingsPageView(
            self.root, self, self.bg_color, self.savings_page_model.get_user_goals(self.user_data)
        )

    def submit_open_goal(self, goal_name):
        goal_info = self.savings_page_model.get_info_about_goal(self.user_data, goal_name)
        time_left = self.savings_page_model.calculate_time_left_for_goal(goal_info[3])
        progress = self.savings_page_model.calculate_percent_of_goal_accomplished(goal_info[2], goal_info[4])
        # fill the overview
        self.savings_page_view.destroy_overview_frame()
        self.savings_page_view.open_goal_overview(goal_info, time_left, progress)

    def delete_goal(self, goal_name):
        result = messagebox.askquestion(title='Warning', message="Do you want to delete this goal?")
        if result == "yes":
            self.savings_page_model.delete_goal_from_database(self.user_data, goal_name)

            self.savings_page_view.initial_overview()
            self.savings_page_view.update_goal_list()
        elif result == "no":
            pass

    def make_new_goal(self):
        self.savings_page_view.make_new_goal_window()

    def bank_deposit(self):
        ...

    def investments(self):
        ...

    def back(self):
        from LoggedUserPage.LoggedUserPageController import LoggedUserPageController
        self.savings_page_view.destroy_savings_frame()
        LoggedUserPageController(self.root, self.user_data, self.bg_color)

    # Make new goal window buttons
    def submit_goal(self, goal_name, goal_amount, goal_date):
        if not self.savings_page_model.goal_name_validation(goal_name):
            messagebox.showinfo("Information", "Your goal has been successfully added!")
            return

        if not self.savings_page_model.goal_amount_validation(goal_amount):
            messagebox.showinfo("Information", "Your goal has been successfully added!")
            return

        self.savings_page_model.save_goal_to_database(self.user_data, goal_name, goal_amount, goal_date, progress=0, automatic_deposit=0)
        self.savings_page_view.destroy_make_goal_window()
        messagebox.showinfo("Information", "Your goal has been successfully added!")

    # Goal Overview buttons
    def deposit(self):
        ...

    def withdraw(self):
        ...

    def save_auto_deposit(self, goal_name, automatic_deposit):
        self.savings_page_model.update_automatic_deposit_in_database(self.user_data, goal_name, automatic_deposit)
        # self.savings_page_model.save_automatic_deposit_to_constants()

        self.savings_page_view.update_auto_deposit_label(automatic_deposit)
