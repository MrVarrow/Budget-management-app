from RateAppWindow.RateAppWindowView import RateAppWindowView
from RateAppWindow.RateAppWindowModel import RateAppWindowsModel
from tkinter import messagebox


class RateAppWindowController:
    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.rate_app_window_view = RateAppWindowView(self.root, self)
        self.rate_app_window_model = RateAppWindowsModel()

    def star_selection(self, user_rating):
        self.rate_app_window_view.get_user_rating(user_rating)
        self.rate_app_window_view.stars_display(user_rating)
        self.rate_app_window_view.your_rating_widget_configure(user_rating)

    def submit_rating(self, final_rating):
        if self.check_if_user_choose(final_rating):
            messagebox.showinfo(title="Information",
                                   message="You have to select number of stars in order to rate app")
            return
        if self.check_if_has_already_rated_app():
            result = messagebox.askquestion(title="Information",
                                   message="You already has rated App. Do you want to change your rating?")
            if result == "yes":
                ...
                # update user rating
            elif result == "no":
                ...
                # close the window

        # Add rate to database
        messagebox.showinfo(title="Information",
                            message="You has successfully rated application. Thanks!")

    def check_if_user_choose(self, final_rating):
        if final_rating == "":
            return False
        return True

    def check_if_has_already_rated_app(self):
        if self.rate_app_window_model.check_if_has_already_rated_app(self.user_data):
            return False
        return True

