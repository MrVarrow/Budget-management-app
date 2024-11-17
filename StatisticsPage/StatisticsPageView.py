from tkinter import *
from tkinter import ttk


class StatisticsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.time_period_list = []
        self.current_period = StringVar()
        self.stats_list = []
        self.current_stat = StringVar()

        # Savings frame
        self.statistics_frame = Frame(self.root, bg=self.bg_color)
        self.statistics_frame.grid()

        # Overview frame
        self.overview_frame_creation()

        # Labels
        Label(self.statistics_frame, text="Your statistics", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=125, pady=23, ipadx=350, ipady=50) \

            # Combobox with goals
        Label(self.statistics_frame, text="Time period:", font=('Arial', 20)) \
            .grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=10)

        self.goals = ttk.Combobox(self.statistics_frame, font=('Arial', 20), values=self.time_period_list,
                                  textvariable=self.current_period, state='readonly')
        self.goals.grid(row=2, column=0, columnspan=2, sticky=W, padx=50)
        self.goals.set("Select time period")

        # Submit open goal button
        Label(self.statistics_frame, text="Stats:", font=('Arial', 20)) \
            .grid(row=3, column=0, columnspan=2, sticky=W, padx=50, pady=10)

        self.stats = ttk.Combobox(self.statistics_frame, font=('Arial', 20), values=self.stats_list,
                                  textvariable=self.current_stat, state='readonly')
        self.stats.grid(row=4, column=0, columnspan=2, sticky=W, padx=50)
        self.stats.set("Select statistic")

        # bank deposit button
        Button(self.statistics_frame, text="Submit", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.bank_deposit()) \
            .grid(row=5, column=0, columnspan=2, sticky=W, padx=100, pady=40)

        # Back button
        Button(self.statistics_frame, text="Back", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: self.controller.back()) \
            .grid(row=6, column=2, sticky=E, padx=20, pady=5)

        # Display initial overview
        self.initial_overview()


# Create overview frame
    def overview_frame_creation(self):
        self.overview_frame = Frame(self.statistics_frame, bg=self.bg_color, borderwidth=2, relief="solid")
        self.overview_frame.grid(row=1, rowspan=5, column=2, sticky=NSEW, padx=80)

    # Create welcome label in overview
    def initial_overview(self):
        Label(self.overview_frame, text="Choose your statistic\n to view", font=('Arial', 35)) \
            .grid(column=0, row=0, sticky=W, padx=130, pady=170)

    def destroy_overview_frame(self):
        self.overview_frame.destroy()

    def destroy_statistics_frame(self):
        self.destroy_statistics_frame()
