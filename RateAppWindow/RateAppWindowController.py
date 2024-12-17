from RateAppWindow.RateAppWindowView import RateAppWindowView
from RateAppWindow.RateAppWindowModel import RateAppWindowsModel
from tkinter import messagebox
from SendEmails import send_email_thanks_for_rate

class RateAppWindowController:
    def __init__(self, root, user_data, bg_color):
        self.bg_color = bg_color
        self.root = root
        self.user_data = user_data
        self.rate_app_window_view = RateAppWindowView(self.root, self, self.bg_color)
        self.rate_app_window_model = RateAppWindowsModel()

    # Manipulation with numbers of stars displayed based on user action
    def star_selection(self, user_rating):
        self.rate_app_window_view.get_user_rating(user_rating)
        self.rate_app_window_view.stars_display()
        self.rate_app_window_view.your_rating_widget_configure(user_rating)

    # Inserting, Updating database or just closing the window
    def submit_rating(self, final_rating):
        if not self.rate_app_window_model.check_if_user_choose(final_rating):
            messagebox.showinfo(title="Information",
                                message="You Have to choose numbers of stars in order to rate the app")
            return
        if not self.rate_app_window_model.check_if_has_already_rated_app(self.user_data):
            result = messagebox.askquestion(title="Information",
                                            message="You already rated us! Your rating is: {} star."
                                                    "Do you Want to change your rating?"
                                            .format(self.rate_app_window_model.user_rating_from_db))
            if result == "yes":
                self.rate_app_window_model.update_user_rating(self.user_data, final_rating)
                self.rate_app_window_view.close_rate_window()
                messagebox.showinfo(title="Information",
                                    message="You has successfully updated your rating. Thanks!")
            elif result == "no":
                self.rate_app_window_view.close_rate_window()
            return

        self.rate_app_window_model.insert_user_rating(self.user_data, final_rating)
        if self.user_data[3] == "1":
            send_email_thanks_for_rate(self.user_data[1], self.user_data[0])
        self.rate_app_window_view.close_rate_window()
        messagebox.showinfo(title="Information",
                            message="You has successfully rated application. Thanks!")
