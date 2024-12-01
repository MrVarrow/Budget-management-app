from tkinter import *
from tkinter import ttk


class StatisticsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables
        self.time_period_list = \
            ["Last Month", "Last 6 Months", "Last Year", "Last 5 Years", "Last 10 Years", "All time"]
        self.current_period = StringVar()
        self.stats_list = ["General stats", "Avg month stats", "Percent stats", "Divided into categories",
                           "The biggest incomes and expenses", "Month budget stats",
                           "Incomes and expenses depending on the month"]
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
               command=lambda: self.controller.submit_stat(self.current_period.get(), self.current_stat.get())) \
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

    '''
    General stats
    '''

    def general_stats_overview(self, all_money_spent, all_money_earned, all_free_amount_left):
        Label(self.overview_frame, text=f"All money spent: {all_money_spent}").grid()

        Label(self.overview_frame, text=f"All money earned: {all_money_earned}").grid()

        Label(self.overview_frame, text=f"All Free amount left: {all_free_amount_left}").grid()

        Label(self.overview_frame, text="Calculate money").grid()
        ttk.Combobox(self.overview_frame).grid()

        Label(self.overview_frame, text="with category").grid()
        ttk.Combobox(self.overview_frame).grid()

        Button(self.overview_frame, text="Submit").grid()

        Label(self.overview_frame, text="Calculate money").grid()

    '''
    Avg month stats
    '''

    def avg_month_stats_overview(self):
        ...

    '''
    Percent stats
    '''

    def percent_stats_overview(self):
        Label(self.overview_frame, text="Percent incomes by category:").grid()

        Label(self.overview_frame, text="Percent expenses by category:").grid()

    '''
    The biggest incomes and expenses
    '''

    def biggest_incomes_expenses_overview(self):
        Label(self.overview_frame, text="Largest amount spent:").grid()
        Label(self.overview_frame, text="This month you spent the most money:").grid()
        Label(self.overview_frame, text="This month you spent less money:").grid()

        Label(self.overview_frame, text="Largest amount gained:").grid()
        Label(self.overview_frame, text="This month you gained the most money:").grid()
        Label(self.overview_frame, text="This month you gained less money:").grid()

        Label(self.overview_frame, text="Largest free amount :").grid()
        Label(self.overview_frame, text="This month you have most free amount:").grid()
        Label(self.overview_frame, text="This month you had less free amount:").grid()

    '''
    Month budget stats
    '''

    def month_budget_stats_overview(self):
        Label(self.overview_frame, text="Money spent").grid()
        Label(self.overview_frame, text="Income").grid()
        Label(self.overview_frame, text="Free amount").grid()

    '''
    Incomes and expenses depending on the month
    '''

    def incomes_expanses_on_month_overview(self):
        Label(self.overview_frame, text="Money spent depending on the month:").grid()

        Label(self.overview_frame, text="Money gained depending on the month:").grid()

        Label(self.overview_frame, text="Free amount left depending on the month:").grid()
