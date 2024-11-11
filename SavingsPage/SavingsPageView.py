from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SavingsPageView:
    def __init__(self, master, controller, bg_color, user_goals):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        self.user_goals = user_goals
        self.current_goal = StringVar()
        self.automatic_deposit = StringVar()
        self.new_auto_deposit = StringVar()
        self.goal_info = []

        # Savings frame
        self.savings_frame = Frame(self.root, bg=self.bg_color)
        self.savings_frame.grid()

        # Overview frame
        self.overview_frame_creation()

        # Labels
        Label(self.savings_frame, text="Your savings", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=135, pady=23, ipadx=350, ipady=50) \

        # Combobox with goals
        self.goals = ttk.Combobox(self.savings_frame, font=('Arial', 20), values=self.user_goals,
                                  textvariable=self.current_goal, state='readonly')
        self.goals.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=40)
        self.goals.set("Select goal")

        # Submit open goal button
        Button(self.savings_frame, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_open_goal(self.goals.get())) \
            .grid(row=2, column=0, sticky=W, padx=50)

        # Delete goal button
        Button(self.savings_frame, text="Delete", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.delete_goal(self.goal_info[1])) \
            .grid(row=2, column=0, columnspan=2, sticky=E, padx=55)

        # Make new goal button
        Button(self.savings_frame, text="Make new goal", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.make_new_goal()) \
            .grid(row=3, column=0, columnspan=2, sticky=W, padx=100, pady=60)

        # Investments button
        Button(self.savings_frame, text="Investments", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.investments()) \
            .grid(row=4, column=0, columnspan=2, sticky=W, padx=100)

        # bank deposit button
        Button(self.savings_frame, text="Bank deposit", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.bank_deposit()) \
            .grid(row=5, column=0, columnspan=2, sticky=W, padx=100, pady=30)

        # Back button
        Button(self.savings_frame, text="Back", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: self.controller.back()) \
            .grid(row=6, column=2, sticky=E, padx=20, pady=5)

        # Display initial overview
        self.initial_overview()

    # Create overview frame
    def overview_frame_creation(self):
        self.overview_frame = Frame(self.savings_frame, bg=self.bg_color, borderwidth=2, relief="solid")
        self.overview_frame.grid(row=1, rowspan=5, column=2, sticky=NSEW, padx=80)

        self.savings_frame.grid_rowconfigure(1, weight=1)
        self.savings_frame.grid_columnconfigure(2, weight=2)

    # Create welcome label in overview
    def initial_overview(self):
        Label(self.overview_frame, text="Choose your goal", font=('Arial', 35)) \
            .grid(column=0, row=0, sticky=W, padx=150, pady=190)

    # Destroy overview frame
    def destroy_overview_frame(self):
        self.overview_frame.destroy()

    # Displays given goal overview
    def open_goal_overview(self, goal_info, time_left, progress):
        self.goal_info = goal_info
        self.overview_frame_creation()

        # Display info for labels
        self.automatic_deposit.set(f"Your actual automatic deposit: {int(goal_info[5])}")
        self.new_auto_deposit.set(goal_info[5])

        # Labels and entries
        Label(self.overview_frame, text=goal_info[1], font=('Arial', 25), bg="light gray", width=30) \
            .grid(row=0, column=0, pady=25, padx=55, sticky=W, ipady=5)

        Label(self.overview_frame, text=f"Goal amount: {goal_info[2]}", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50, pady=10)

        Label(self.overview_frame, text=f"Goal date: {goal_info[3]}", font=('Arial', 15)) \
            .grid(row=2, column=0, sticky=W, padx=50, pady=10)

        Label(self.overview_frame, textvariable=self.automatic_deposit, font=('Arial', 15)) \
            .grid(row=4, column=0, sticky=W, padx=20, pady=10)
        Entry(self.overview_frame, textvariable=self.new_auto_deposit, font=('Arial', 15), width=15) \
            .grid(row=5, column=0, sticky=W, padx=30, pady=10)

        Label(self.overview_frame, text="per month", font=('Arial', 15)) \
            .grid(row=5, column=0, sticky=W, padx=200, pady=10)

        # Deposit to goal button
        Button(self.overview_frame, text="Deposit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.deposit()) \
            .grid(row=3, column=0, sticky=W, padx=20, pady=10)

        # Withdraw from goal button
        Button(self.overview_frame, text="Withdraw", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.withdraw()) \
            .grid(row=3, column=0, sticky=W, padx=170, pady=10)

        # Save automatic deposit button
        Button(self.overview_frame, text="Save", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.save_auto_deposit(goal_info[1], self.new_auto_deposit.get(),
                                                                 self.goal_info[2])) \
            .grid(row=6, column=0, sticky=W, padx=100, pady=10)

        self.progress_bar = ttk.Progressbar(self.overview_frame, orient=HORIZONTAL, length=300, mode="determinate",
                                            variable=goal_info[4], maximum=100, value=progress)
        self.progress_bar.grid(row=1, column=0, sticky=E, padx=50, pady=10)

        self.progress_label = Label(self.overview_frame,
                                    text=f"You have achieved {progress}% of your goal.\nCongratulations!",
                                    font=('Arial', 15))
        self.progress_label.grid(row=2, column=0, sticky=E, padx=30, pady=10)

        self.collect_label = Label(self.overview_frame, text=f"Collected {goal_info[4]} from {goal_info[2]}",
                                   font=('Arial', 15), width=30)
        self.collect_label.grid(row=3, column=0, sticky=E, padx=30, pady=10)

        Label(self.overview_frame, text=f"Time left: \n{time_left}", font=('Arial', 15)) \
            .grid(row=4, rowspan=3, column=0, sticky=E, padx=140, pady=40)

    # Updates display value of automatic deposit
    def update_auto_deposit_label(self, automatic_deposit):
        self.automatic_deposit.set(f"Your actual automatic deposit: {automatic_deposit}")

    # Updates display of progress made
    def update_progress(self, progress, goal_info):
        self.progress_label.configure(text=f'You have achieved {progress}% of your goal.\nCongratulations!')
        self.progress_bar.configure(value=progress)
        self.collect_label.configure(text=f'Collected {goal_info[4]} from {goal_info[2]}')

    # Updates user goals list
    def update_goal_list(self, user_goals):
        self.goals.configure(values=user_goals)

    # Displays new goal creation window
    def make_new_goal_window(self):
        self.make_goal_window = Toplevel(self.root, bg=self.bg_color)
        self.make_goal_window.geometry("400x200")
        self.make_goal_window.title("Make new goal")
        self.make_goal_window.resizable(False, False)

        goal_name_var = StringVar()
        goal_amount_var = StringVar()

        # Labels and entries
        Label(self.make_goal_window, text="Goal name:", font=('Arial', 12)) \
            .grid(row=0, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15), textvariable=goal_name_var) \
            .grid(row=1, column=0, padx=100, sticky=W)

        Label(self.make_goal_window, text="Goal amount:", font=('Arial', 12)) \
            .grid(row=2, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15), textvariable=goal_amount_var) \
            .grid(row=3, column=0, padx=100, sticky=W)

        Label(self.make_goal_window, text="Goal date:", font=('Arial', 12)) \
            .grid(row=4, column=0, padx=100, sticky=W)

        # DateEntry
        cal = DateEntry(self.make_goal_window, width=12, background='light gray', foreground='black', borderwidth=2,
                        date_pattern='yyyy-mm-dd', font=('Arial', 12))
        cal.grid(row=5, column=0, padx=145, sticky=W, pady=5)

        # Submit goal
        Button(self.make_goal_window, text="Submit goal", font=('Arial', 15), bg="light gray",
               command=lambda: self.controller.submit_goal(
                   goal_name_var.get(), goal_amount_var.get(), cal.get_date())) \
            .grid(row=6, column=0, padx=150, sticky=W)

        # Focus on TopLevel window
        self.make_goal_window.grab_set()

    # Destroys savings frame
    def destroy_savings_frame(self):
        self.savings_frame.destroy()

    # Destroys make new goal window
    def destroy_make_goal_window(self):
        self.make_goal_window.destroy()

    # Displays deposit window
    def deposit_window(self):
        self.deposit_window_1 = Toplevel(self.root, bg=self.bg_color)
        self.deposit_window_1.geometry("400x200")
        self.deposit_window_1.title("Make new goal")
        self.deposit_window_1.resizable(False, False)

        deposit_amount = StringVar()

        # Labels and entries
        Label(self.deposit_window_1, text="Enter deposit amount:", font=('Arial', 15))\
            .grid(row=0, column=0, sticky=W, padx=100, pady=20)
        Entry(self.deposit_window_1, textvariable=deposit_amount, font=('Arial', 15), width=15) \
            .grid(row=1, column=0, sticky=W, padx=115, pady=10)

        # Submit deposit amount button
        Button(self.deposit_window_1, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_deposit(deposit_amount.get(),
                                                              self.goal_info[1], self.goal_info[2]))\
            .grid(row=2, column=0, sticky=W, padx=140, pady=30)

        # Focus on TopLevel window
        self.deposit_window_1.grab_set()

    # Displays withdraw window
    def withdraw_window(self):
        self.withdraw_window_1 = Toplevel(self.root, bg=self.bg_color)
        self.withdraw_window_1.geometry("400x200")
        self.withdraw_window_1.title("Make new goal")
        self.withdraw_window_1.resizable(False, False)

        withdraw_amount = StringVar()

        # Labels and entries
        Label(self.withdraw_window_1, text="Enter withdraw amount:", font=('Arial', 15)) \
            .grid(row=0, column=0, sticky=W, padx=100, pady=20)
        Entry(self.withdraw_window_1, textvariable=withdraw_amount, font=('Arial', 15), width=15) \
            .grid(row=1, column=0, sticky=W, padx=115, pady=10)

        # Submit withdraw amount button
        Button(self.withdraw_window_1, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_withdraw(withdraw_amount.get(),
                                                               self.goal_info[1], self.goal_info[2])) \
            .grid(row=2, column=0, sticky=W, padx=140, pady=30)

        # Focus on TopLevel window
        self.withdraw_window_1.grab_set()

    # Destroys deposit window
    def destroy_deposit_window(self):
        self.deposit_window_1.destroy()

    # Destroys withdraw window
    def destroy_withdraw_window(self):
        self.withdraw_window_1.destroy()

    # Displays investments overview
    def investments_overview(self):
        self.overview_frame_creation()

        # Entry variables define
        entry_payment = StringVar()
        future_payments = StringVar()
        frequency_of_payments = StringVar()
        frequency_vals = {"Yearly": 1, "Monthly": 12}
        investing_time = StringVar()
        rate_of_return = StringVar()
        self.total_value_info = StringVar()

        # Set message for total value label
        self.total_value_info.set("At the end you will make:")

        # Labels and entries
        Label(self.overview_frame, text="Investments calculator", font=('Arial', 25), bg="light gray", width=30) \
            .grid(row=0, column=0, pady=25, padx=55, sticky=W, ipady=5)

        Label(self.overview_frame, text="Entry payment:", font=('Arial', 12), width=20) \
            .grid(row=1, column=0, padx=50, sticky=W)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=entry_payment) \
            .grid(row=2, column=0, padx=50, sticky=W, pady=10)

        Label(self.overview_frame, text="Future payments:", font=('Arial', 12), width=20) \
            .grid(row=1, column=0)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=future_payments) \
            .grid(row=2, column=0, pady=10)

        Label(self.overview_frame, text="Frequency of payments:", font=('Arial', 12), width=20) \
            .grid(row=1, column=0, padx=50, sticky=E)
        ttk.Combobox(self.overview_frame, font=('Arial', 12), width=18, textvariable=frequency_of_payments,
                     values=list(frequency_vals.keys()), state='readonly') \
            .grid(row=2, column=0, padx=50, sticky=E, pady=10)

        Label(self.overview_frame, text="Investing time in years:", font=('Arial', 12), width=20) \
            .grid(row=3, column=0, padx=150, sticky=W, pady=10)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=investing_time) \
            .grid(row=4, column=0, padx=150, sticky=W)

        Label(self.overview_frame, text="Rate of return per year:", font=('Arial', 12), width=20) \
            .grid(row=3, column=0, padx=150, sticky=E, pady=10)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=rate_of_return) \
            .grid(row=4, column=0, padx=150, sticky=E)

        Label(self.overview_frame, textvariable=self.total_value_info, font=('Arial', 15), width=45, height=2) \
            .grid(row=6, column=0)

        # Calculate value of investments button
        Button(self.overview_frame, text="Calculate", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.confirm_calculate_investments(
                   str(entry_payment.get()), str(future_payments.get()),
                   str(frequency_vals[frequency_of_payments.get()]),
                   str(investing_time.get()),  str(rate_of_return.get())
               )) \
            .grid(row=5, column=0, pady=20)

        # Check graph button
        Button(self.overview_frame, text="Check graph", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.create_graph()) \
            .grid(row=7, column=0, pady=10, padx=150, sticky=W)

        # Check table button
        Button(self.overview_frame, text="Check table", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.create_table()) \
            .grid(row=7, column=0, pady=10, padx=150, sticky=E)

    # Updates total value of investments label
    def update_total_value_label(self, total_value):
        self.total_value_info.set(f"At the end you will make: \n {total_value}")

    # Displays bank deposit overview
    def bank_deposit_overview(self):
        self.overview_frame_creation()

        # Entry variables define
        amount = StringVar()
        capitalization_time = StringVar()
        capitalization_vals = {"Yearly": 1, "Monthly": 12, "Quarter": 4, "At the end": 0}
        bank_deposit_time = StringVar()
        interest_rate = StringVar()
        self.total_value_info = StringVar()

        # Set message for total value label
        self.total_value_info.set("At the end you will make:")

        # Labels and entries
        Label(self.overview_frame, text="Bank deposit calculator", font=('Arial', 25), bg="light gray", width=30) \
            .grid(row=0, column=0, pady=25, padx=55, sticky=W, ipady=5)

        Label(self.overview_frame, text="Amount:", font=('Arial', 12), width=20) \
            .grid(row=1, column=0, padx=100, sticky=W)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=amount) \
            .grid(row=2, column=0, padx=100, sticky=W, pady=10)

        Label(self.overview_frame, text="Bank deposit time in years:", font=('Arial', 12), width=20) \
            .grid(row=1, column=0, padx=100, sticky=E)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=bank_deposit_time) \
            .grid(row=2, column=0, padx=100, sticky=E, pady=10)

        Label(self.overview_frame, text="Interest rate:", font=('Arial', 12), width=20) \
            .grid(row=3, column=0, padx=100, sticky=W, pady=10)
        Entry(self.overview_frame, font=('Arial', 12), width=20, textvariable=interest_rate) \
            .grid(row=4, column=0, padx=100, sticky=W)

        Label(self.overview_frame, text="capitalization time:", font=('Arial', 12), width=20) \
            .grid(row=3, column=0, padx=100, sticky=E, pady=10)
        ttk.Combobox(self.overview_frame, font=('Arial', 12), width=18, textvariable=capitalization_time,
                     values=list(capitalization_vals.keys()), state='readonly') \
            .grid(row=4, column=0, padx=100, sticky=E)

        Label(self.overview_frame, textvariable=self.total_value_info, font=('Arial', 15), width=45, height=2)\
            .grid(row=6, column=0)

        # Calculate bank deposit value button
        Button(self.overview_frame, text="Calculate", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.confirm_calculate_bank_deposit(
                   str(amount.get()), str(bank_deposit_time.get()), str(interest_rate.get()),
                   str(capitalization_vals[capitalization_time.get()]))
               ) \
            .grid(row=5, column=0, pady=20)

        # Check graph button
        Button(self.overview_frame, text="Check graph", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.create_graph()) \
            .grid(row=7, column=0, pady=10, padx=150, sticky=W)

        # Check table button
        Button(self.overview_frame, text="Check table", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.create_table()) \
            .grid(row=7, column=0, pady=10, padx=150, sticky=E)

    # Creates graph in new window
    def create_graph(self, fig):
        graph_window = Toplevel(self.root, bg=self.bg_color)
        graph_window.resizable(False, False)
        graph_window.title("Investments value graph")

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        canvas.draw()

        graph_window.grab_set()

    # Creates table in new window
    def create_table(self, profit_df):
        table_window = Toplevel(self.root, bg=self.bg_color)
        table_window.resizable(False, False)
        table_window.title("Investments value table")

        columns = list(profit_df.columns)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="light green", foreground='black')

        table_treeview = ttk.Treeview(table_window, columns=columns, show='headings',
                                      height=len(list(profit_df.iterrows())))

        table_treeview.tag_configure('oddrow', background='light blue')
        table_treeview.tag_configure('evenrow', background='lightgrey')
        for col in columns:
            if col == "year":
                table_treeview.column(col, anchor=CENTER, width=50)
            else:
                table_treeview.column(col, anchor=CENTER, width=200)

            table_treeview.heading(col, text=col)

        table_treeview.pack(fill=BOTH, expand=True)

        for item in table_treeview.get_children():
            table_treeview.delete(item)

        # Insert new data into the treeview
        for index, row in profit_df.iterrows():
            row = [int(row[0]), row[1]]
            if index % 2 == 0:
                table_treeview.insert("", END, values=list(row), tags=('oddrow',))
            else:
                table_treeview.insert("", END, values=list(row), tags=('evenrow',))

        table_window.grab_set()
