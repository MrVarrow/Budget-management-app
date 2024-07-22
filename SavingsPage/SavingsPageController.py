from tkinter import messagebox
from SavingsPage.SavingsPageView import SavingsPageView
from SavingsPage.SavingsPageModel import SavingsPageModel


class SavingsPageController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.savings_page_model = SavingsPageModel()
        self.savings_page_view = SavingsPageView(self.root, self, self.bg_color)

    def submit_open_goal(self):
        ...

    def delete_goal(self):
        ...

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
        self.savings_page_model.save_goal_to_database(goal_name, goal_amount, goal_date)
        self.savings_page_view.destroy_make_goal_window()
        messagebox.showinfo("Information", "Your goal has been successfully added!")
