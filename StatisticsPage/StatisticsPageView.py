from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
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
        self.stats_list = ["General stats", "Avg month stats", "Percent stats",
                           "The biggest incomes and expenses", "Incomes and expenses depending on the month"]
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
        Label(self.overview_frame, text=f"All money spent: {all_money_spent}", font=('Arial', 15)) \
            .grid(row=0, rowspan=2, column=0, sticky=W, padx=50, pady=50)

        Label(self.overview_frame, text=f"All money earned: {all_money_earned}", font=('Arial', 15)) \
            .grid(row=1, rowspan=2, column=0, sticky=W, padx=50, pady=50)

        Label(self.overview_frame, text=f"All Free amount left: {all_free_amount_left}", font=('Arial', 15)) \
            .grid(row=2, rowspan=2, column=0, sticky=W, padx=50, pady=50)

        Label(self.overview_frame, text="Calculate money", font=('Arial', 15)) \
            .grid(row=0, column=1, sticky=W, pady=20)
        self.type_combobox = ttk.Combobox(self.overview_frame, values=["spent", "earned"], textvariable=self.chosen_type, state="readonly", font=('Arial', 15))
        self.type_combobox.grid(row=1, column=1, sticky=W, pady=20)
        self.type_combobox.bind('<<ComboboxSelected>>', lambda event: self.update_second_combobox(categories_incomes,
                               categories_expenses))

        Label(self.overview_frame, text="with category", font=('Arial', 15)) \
            .grid(row=2, column=1, sticky=W, pady=20)
        self.category_combobox = ttk.Combobox(self.overview_frame, state="disabled", textvariable=self.chosen_category, font=('Arial', 15))
        self.category_combobox.set('Choose type first')
        self.category_combobox.grid(row=3, column=1, sticky=W, pady=20)


        Button(self.overview_frame, text="Submit", command=lambda: self.controller.submit_category(self.chosen_type.get(), self.chosen_category.get()), font=('Arial', 15), width=10, bg="light gray") \
            .grid(row=4, column=1, sticky=W, padx=70, pady=20)

        self.result_label = Label(self.overview_frame, text="Result of Calculations", font=('Arial', 15), width=30)
        self.result_label.grid(row=5, column=0, columnspan=2, sticky=W, padx=150, pady=35)

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
        Label(self.overview_frame, text=f"Average money spent per month: \n\n{avg_spent}", font=('Arial', 15), width=50, height=3) \
            .grid(row=0, column=0, sticky=W, padx=50, pady=30)

        Label(self.overview_frame, text=f"Average money earned per month: \n\n{avg_earned}", font=('Arial', 15), width=50, height=3) \
            .grid(row=1, column=0, sticky=W, padx=50, pady=40)

        Label(self.overview_frame, text=f"Average Free amount left per month: \n\n{avg_free_amount}", font=('Arial', 15), width=50, height=3) \
            .grid(row=2, column=0, sticky=W, padx=50, pady=30)

    '''
    Percent stats
    '''

    def percent_stats_overview(self, incomes_category_percentage_dict, expenses_category_percentage_dict):
        # Check if there are any categories to display
        if not incomes_category_percentage_dict and not expenses_category_percentage_dict:
            return
        self.overview_frame_creation()

        # Prepare data for the income pie chart
        income_categories = list(incomes_category_percentage_dict.keys())
        income_amounts = [data['amount'] for data in incomes_category_percentage_dict.values()]

        # Create a Matplotlib figure with 2 subplots
        fig, axs = plt.subplots(1, 2, figsize=(7, 4.5), dpi=100)  # Adjust figsize as needed

        # Create the income pie chart
        axs[0].pie(income_amounts, labels=income_categories, autopct='%1.1f%%', startangle=140)
        axs[0].set_title("Income by Category:")

        # Prepare data for the expense pie chart
        expense_categories = list(expenses_category_percentage_dict.keys())
        expense_amounts = [data['amount'] for data in expenses_category_percentage_dict.values()]

        # Create the expense pie chart
        axs[1].pie(expense_amounts, labels=expense_categories, autopct='%1.1f%%', startangle=140)
        axs[1].set_title("Expenses by Category:")

        # Adjust spacing between subplots and frame borders
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1,
                            wspace=0.2)  # Adjust wspace for horizontal spacing

        # Optionally use tight_layout() to further refine spacing
        fig.tight_layout(pad=2.0)  # You can adjust the padding as needed

        # Create a canvas to display the figure in the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.overview_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    '''
    The biggest incomes and expenses
    '''

    def biggest_incomes_expenses_overview(self, max_income_category, max_income_value, max_expenses_category,
                                          max_expenses_value, max_income_month, max_income, min_income_month,
                                          min_income, max_expense_month, max_expense, min_expense_month, min_expense,
                                          max_free_amount_month, max_free_amount, min_free_amount_month,
                                          min_free_amount):
        self.overview_frame_creation()

        Label(self.overview_frame, text=f"Largest spending: \n{max_expenses_value} at {max_expenses_category}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=0, column=0, sticky=W, padx=50, pady=5)
        Label(self.overview_frame, text=f"In this month you spent the most money: \n{max_expense} at {max_expense_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=1, column=0, sticky=W, padx=50)
        Label(self.overview_frame, text=f"In this month you spent the least amount of money: \n{min_expense} at {min_expense_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=2, column=0, sticky=W, padx=50, pady=5)

        Label(self.overview_frame, text=f"Largest earning: \n{max_income_value} at {max_income_category}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=3, column=0, sticky=W, padx=50)
        Label(self.overview_frame, text=f"In this month, you earned the most money: \n{max_income} at {max_income_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=4, column=0, sticky=W, padx=50, pady=5)
        Label(self.overview_frame, text=f"In this month you earned the least amount of money: \n{min_income} at {min_income_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=5, column=0, sticky=W, padx=50)

        Label(self.overview_frame, text=f"This month, you have the highest amount of free funds: \n{max_free_amount} at {max_free_amount_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=6, column=0, sticky=W, padx=50, pady=5)
        Label(self.overview_frame, text=f"This month, you have the lowest amount of free funds: \n{min_free_amount} at {min_free_amount_month}", font=('Arial', 15), width=50, height=2, justify='left', anchor='w') \
            .grid(row=7, column=0, sticky=W, padx=50)

    '''
    Incomes and expenses depending on the month
    '''

    def incomes_expanses_on_month_overview(self, incomes_dict, expenses_dict):
        # Check if there are any categories to display
        if not incomes_dict and not expenses_dict:
            return

        self.overview_frame_creation()

        # Prepare data for the income pie chart
        income_categories = list(incomes_dict.keys())
        income_amounts = [float(amount) for amount in incomes_dict.values()]  # Convert Decimal to float

        # Create a Matplotlib figure with 2 subplots
        fig, axs = plt.subplots(1, 2, figsize=(7, 4.5), dpi=100)  # Adjust figsize as needed

        # Create the income pie chart
        axs[0].pie(income_amounts, labels=income_categories, autopct='%1.1f%%', startangle=140)
        axs[0].set_title("Income by Month:")

        # Prepare data for the expense pie chart
        expense_categories = list(expenses_dict.keys())
        expense_amounts = [float(amount) for amount in expenses_dict.values()]  # Convert Decimal to float

        # Create the expense pie chart
        axs[1].pie(expense_amounts, labels=expense_categories, autopct='%1.1f%%', startangle=140)
        axs[1].set_title("Expenses by Month:")

        # Adjust spacing between subplots and frame borders
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1,
                            wspace=0.2)  # Adjust wspace for horizontal spacing

        # Optionally use tight_layout() to further refine spacing
        fig.tight_layout(pad=2.0)  # You can adjust the padding as needed

        # Create a canvas to display the figure in the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.overview_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
