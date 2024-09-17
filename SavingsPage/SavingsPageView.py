from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry


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

        goals = ttk.Combobox(self.savings_frame, font=('Arial', 20), values=self.user_goals,
                             textvariable=self.current_goal)
        goals.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=40)

        Button(self.savings_frame, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_open_goal(goals.get())) \
            .grid(row=2, column=0, sticky=W, padx=50)

        Button(self.savings_frame, text="Delete", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.delete_goal()) \
            .grid(row=2, column=0, columnspan=2, sticky=E, padx=55)

        Button(self.savings_frame, text="Make new goal", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.make_new_goal()) \
            .grid(row=3, column=0, columnspan=2, sticky=W, padx=100, pady=60)

        Button(self.savings_frame, text="Investments", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.investments()) \
            .grid(row=4, column=0, columnspan=2, sticky=W, padx=100)

        Button(self.savings_frame, text="Bank deposit", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.bank_deposit()) \
            .grid(row=5, column=0, columnspan=2, sticky=W, padx=100, pady=30)

        Button(self.savings_frame, text="Back", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: self.controller.back()) \
            .grid(row=6, column=2, sticky=E, padx=20, pady=5)

        self.initial_overview()

    def overview_frame_creation(self):
        self.overview_frame = Frame(self.savings_frame, bg=self.bg_color, borderwidth=2, relief="solid")
        self.overview_frame.grid(row=1, rowspan=5, column=2, sticky=NSEW, padx=80)

        self.savings_frame.grid_rowconfigure(1, weight=1)
        self.savings_frame.grid_columnconfigure(2, weight=2)

    def initial_overview(self):
        Label(self.overview_frame, text="Choose your goal").grid()

    def destroy_overview_frame(self):
        self.overview_frame.destroy()

    def open_goal_overview(self, goal_info, time_left, progress):
        self.goal_info = goal_info
        self.overview_frame_creation()
        self.automatic_deposit.set(f"Your actual automatic deposit: {goal_info[5]}")
        self.new_auto_deposit.set(goal_info[5])


        # Name
        Label(self.overview_frame, text=goal_info[1], font=('Arial', 25), bg="light gray", width=30) \
            .grid(row=0, column=0, pady=25, padx=55, sticky=W, ipady=5)

        # Goal amount
        Label(self.overview_frame, text=f"Goal amount: {goal_info[2]}", font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=50, pady=10)

        # Goal date
        Label(self.overview_frame, text=f"Goal date: {goal_info[3]}", font=('Arial', 15)) \
            .grid(row=2, column=0, sticky=W, padx=50, pady=10)

        Button(self.overview_frame, text="Deposit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.deposit()) \
            .grid(row=3, column=0, sticky=W, padx=20, pady=10)

        Button(self.overview_frame, text="Withdraw", font=('Arial', 15), bg="light gray", width=10, command=lambda: self.controller.withdraw()) \
            .grid(row=3, column=0, sticky=W, padx=170, pady=10)

        Label(self.overview_frame, textvariable=self.automatic_deposit, font=('Arial', 15)) \
            .grid(row=4, column=0, sticky=W, padx=20, pady=10)

        Entry(self.overview_frame, textvariable=self.new_auto_deposit, font=('Arial', 15), width=15) \
            .grid(row=5, column=0, sticky=W, padx=30, pady=10)

        Label(self.overview_frame, text="per month", font=('Arial', 15)) \
            .grid(row=5, column=0, sticky=W, padx=200, pady=10)

        Button(self.overview_frame, text="Save", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.save_auto_deposit(goal_info[1], self.new_auto_deposit.get())) \
            .grid(row=6, column=0, sticky=W, padx=100, pady=10)

        ttk.Progressbar(self.overview_frame, orient=HORIZONTAL, length=300, mode="determinate", variable=goal_info[4],
                        maximum=100, value=progress) \
            .grid(row=1, column=0, sticky=E, padx=50, pady=10)

        Label(self.overview_frame, text=f"You have achieved {progress}% of your goal.\nCongratulations!"
              , font=('Arial', 15)) \
            .grid(row=2, column=0, sticky=E, padx=30, pady=10)

        Label(self.overview_frame, text=f"Collected {goal_info[4]} from {goal_info[2]}", font=('Arial', 15), width=30)\
            .grid(row=3, column=0, sticky=E, padx=30, pady=10)

        Label(self.overview_frame, text=f"Time left: \n{time_left} days", font=('Arial', 15)) \
            .grid(row=4, rowspan=3, column=0, sticky=E, padx=140, pady=40)

    def update_auto_deposit_label(self, automatic_deposit):
        self.automatic_deposit.set(f"Your actual automatic deposit: {automatic_deposit}")

    def update_progress(self):
        ...

    def update_goal_list(self):
        ...

    def make_new_goal_window(self):
        self.make_goal_window = Toplevel(self.root, bg=self.bg_color)
        self.make_goal_window.geometry("400x200")
        self.make_goal_window.title("Make new goal")
        self.make_goal_window.resizable(False, False)

        goal_name_var = StringVar()
        goal_amount_var = StringVar()

        # Goal name
        Label(self.make_goal_window, text="Goal name:", font=('Arial', 12)) \
            .grid(row=0, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15), textvariable=goal_name_var) \
            .grid(row=1, column=0, padx=100, sticky=W)

        # Goal amount
        Label(self.make_goal_window, text="Goal amount:", font=('Arial', 12)) \
            .grid(row=2, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15), textvariable=goal_amount_var) \
            .grid(row=3, column=0, padx=100, sticky=W)

        # Goal date
        Label(self.make_goal_window, text="Goal date:", font=('Arial', 12)) \
            .grid(row=4, column=0, padx=100, sticky=W)

        # DateEntry
        cal = DateEntry(self.make_goal_window, width=12, background='light gray', foreground='black', borderwidth=2,
                        date_pattern='yyyy-mm-dd', font=('Arial', 12))
        cal.grid(row=5, column=0, padx=145, sticky=W, pady=5)

        # Submit goal
        Button(self.make_goal_window, text="Submit goal", font=('Arial', 15), bg="light gray",
               command=lambda: self.controller.submit_goal(goal_name_var.get(), goal_amount_var.get(), cal.get_date())) \
            .grid(row=6, column=0, padx=150, sticky=W)

        # Focus on TopLevel window
        self.make_goal_window.grab_set()

    def destroy_savings_frame(self):
        self.savings_frame.destroy()

    def destroy_make_goal_window(self):
        self.make_goal_window.destroy()

    def deposit_window(self):
        self.deposit_window = Toplevel(self.root, bg=self.bg_color)
        self.deposit_window.geometry("400x200")
        self.deposit_window.title("Make new goal")
        self.deposit_window.resizable(False, False)

        deposit_amount = StringVar()

        Label(self.deposit_window, text="Enter deposit amount:", font=('Arial', 15))\
            .grid(row=0, column=0, sticky=W, padx=100, pady=20)

        Entry(self.deposit_window, textvariable=deposit_amount, font=('Arial', 15), width=15) \
            .grid(row=1, column=0, sticky=W, padx=115, pady=10)

        Button(self.deposit_window, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_deposit(deposit_amount.get(), self.goal_info[1]))\
            .grid(row=2, column=0, sticky=W, padx=140, pady=30)

        # Focus on TopLevel window
        self.deposit_window.grab_set()

    def withdraw_window(self):
        self.withdraw_window = Toplevel(self.root, bg=self.bg_color)
        self.withdraw_window.geometry("400x200")
        self.withdraw_window.title("Make new goal")
        self.withdraw_window.resizable(False, False)

        withdraw_amount = StringVar()

        Label(self.deposit_window, text="Enter withdraw amount:", font=('Arial', 15)) \
            .grid(row=0, column=0, sticky=W, padx=100, pady=20)

        Entry(self.deposit_window, textvariable=withdraw_amount, font=('Arial', 15)) \
            .grid(row=1, column=0, sticky=W, padx=115, pady=10)

        Button(self.deposit_window, text="Submit", font=('Arial', 15), bg="light gray",
               command=lambda: self.controller.submit_withdraw(withdraw_amount.get(), self.goal_info[1])) \
            .grid(row=2, column=0, sticky=W, padx=140, pady=30)

        # Focus on TopLevel window
        self.withdraw_window.grab_set()

    def destroy_deposit_window(self):
        self.deposit_window.destroy()

    def destroy_withdraw_window(self):
        self.withdraw_window.destroy()
