from tkinter import *


class RateAppWindowView:
    def __init__(self, master, controller, bg_color):
        self.bg_color = bg_color
        self.controller = controller
        self.star_list = ["1", "2", "3", "4", "5"]
        self.filled_star_list = []
        self.unfilled_star_list = []
        self.final_rating = ""
        # Icons loading from Icons folder
        self.empty_star = PhotoImage(file="Icons/empty_star.png")
        self.empty_star = self.empty_star.subsample(20, 20)
        self.full_star = PhotoImage(file="Icons/full_star.png")
        self.full_star = self.full_star.subsample(20, 20)

        self.rate_us_root = Toplevel(master, bg=self.bg_color)
        self.rate_us_root.geometry("400x200")
        self.rate_us_root.title("Rate us!")
        self.rate_us_root.resizable(False, False)

        # Stars Frame creation
        self.rate_us_stars_frame = Frame(self.rate_us_root, bg=self.bg_color)
        self.rate_us_stars_frame.grid(row=1, column=0)

        # Labels
        Label(self.rate_us_root, text="Rate our app!", font=('Arial', 15), bg=self.bg_color) \
            .grid(row=0, column=0, padx=135, pady=15, sticky=W)

        self.user_rate_widget = Label(self.rate_us_root, text="Your rating:\n", font=('Arial', 12), bg=self.bg_color)
        self.user_rate_widget.grid(row=2, column=0, sticky=W, padx=150, pady=10)

        # Star buttons
        i = 100
        for star in self.star_list:
            Button(self.rate_us_stars_frame, image=self.empty_star, bg="light gray",
                   command=lambda user_rating=star: controller.star_selection(user_rating)) \
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40

        # Submit rating button
        Button(self.rate_us_root, text="Submit", font=('Arial', 15), width=7, bg="light gray",
               command=lambda: controller.submit_rating(self.final_rating)).grid(row=3, column=0, sticky=W, padx=150)

        # Focus on TopLevel window
        self.rate_us_root.grab_set()

    # Display number of stars which user rated the app
    def your_rating_widget_configure(self, user_rating):
        self.user_rate_widget.configure(text="Your rating:\n {} star".format(user_rating))
        self.final_rating = user_rating

    # Displaying filled/unfilled stars
    def stars_display(self):
        self.rate_us_stars_frame.destroy()
        self.rate_us_stars_frame = Frame(self.rate_us_root, bg=self.bg_color)
        self.rate_us_stars_frame.grid(row=1, column=0)
        i = 100
        for star in self.filled_star_list:
            Button(self.rate_us_stars_frame, image=self.full_star, bg="light gray",
                   command=lambda new_rating=star: self.controller.star_selection(new_rating)) \
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40
        for star in self.unfilled_star_list:
            Button(self.rate_us_stars_frame, image=self.empty_star, bg="light gray",
                   command=lambda new_rating=star: self.controller.star_selection(new_rating)) \
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40

    # Getting info about stars that have to be filled/unfilled
    def get_user_rating(self, user_rating):
        self.filled_star_list = []
        self.unfilled_star_list = []
        for i in range(0, int(user_rating)):
            x = self.star_list[i]
            self.filled_star_list.append(x)

        for item in range(int(user_rating), len(self.star_list)):
            x = self.star_list[item]
            self.unfilled_star_list.append(x)

    # Destroying window
    def close_rate_window(self):
        self.rate_us_root.destroy()
