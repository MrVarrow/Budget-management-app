from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

    def general_stats_overview(self, all_money_spent, all_money_earned, all_free_amount_left, categories_incomes,
                               categories_expenses):
        self.overview_frame_creation()
        self.chosen_type = StringVar()
        self.chosen_category = StringVar()
        self.chosen_type.set("Choose type")
        Label(self.overview_frame, text=f"All money spent: {all_money_spent}").grid()

        Label(self.overview_frame, text=f"All money earned: {all_money_earned}").grid()

        Label(self.overview_frame, text=f"All Free amount left: {all_free_amount_left}").grid()

        Label(self.overview_frame, text="Calculate money").grid()
        self.type_combobox = ttk.Combobox(self.overview_frame, values=["spent", "earned"], textvariable=self.chosen_type, state="readonly")
        self.type_combobox.grid()
        self.type_combobox.bind('<<ComboboxSelected>>', lambda event: self.update_second_combobox(categories_incomes,
                               categories_expenses))

        Label(self.overview_frame, text="with category").grid()
        self.category_combobox = ttk.Combobox(self.overview_frame, state="disabled", textvariable=self.chosen_category)
        self.category_combobox.set('Choose type first')
        self.category_combobox.grid()


        Button(self.overview_frame, text="Submit", command=lambda: self.controller.submit_category(self.chosen_type.get(), self.chosen_category.get())).grid()

        self.result_label = Label(self.overview_frame, text="Result of Calculations")
        self.result_label.grid()

    def update_second_combobox(self, categories_incomes,
                               categories_expenses):
        self.category_combobox.set('choose category')
        self.category_combobox.configure(state="readonly")

        # Get selected value from the first combo box
        selected_value = self.chosen_type.get()

        # Update second combo box based on selection
        if selected_value == 'spent':
            self.category_combobox['values'] = categories_expenses
        elif selected_value == 'earned':
            self.category_combobox['values'] = categories_incomes

        # Optionally, set the first item as selected in the second combo box if available
        if self.category_combobox['values']:
            self.category_combobox.current(0)


    def display_result(self, result, type, category):
        type_info = ""
        if type == "spent":
            type_info = "spending"
        elif type == "earned":
            type_info = "earnings"
        self.result_label.configure(text=f"Yours {type_info} on {category}: {result}")
    '''
    Avg month stats
    '''

    def avg_month_stats_overview(self, avg_spent, avg_earned, avg_free_amount):
        self.overview_frame_creation()
        Label(self.overview_frame, text=f"Average money spent per month: {avg_spent}").grid()

        Label(self.overview_frame, text=f"Average money earned per month: {avg_earned}").grid()

        Label(self.overview_frame, text=f"Average Free amount left per month: {avg_free_amount}").grid()


    '''
    Percent stats
    '''

    def percent_stats_overview(self, incomes_category_percentage_dict):
        # Check if there are any categories to display
        if not incomes_category_percentage_dict:
            return
        self.overview_frame_creation()

        # Prepare data for the pie chart
        categories = list(incomes_category_percentage_dict.keys())
        amounts = [data['amount'] for data in incomes_category_percentage_dict.values()]

        # Create a Matplotlib figure
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Create a pie chart
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        ax.set_title("Spending by Category")

        # Create a canvas to display the figure in the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.overview_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)

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
