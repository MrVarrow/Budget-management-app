from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry


class SavingsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color
        self.user_goals = []
        self.current_goal = StringVar()

        # Savings frame
        self.savings_frame = Frame(self.root, bg=self.bg_color)
        self.savings_frame.grid()

        # Overview frame
        self.overview_frame = Frame(self.savings_frame, bg=self.bg_color, borderwidth=2, relief="solid")
        self.overview_frame.grid(row=1, rowspan=5, column=0, columnspan=2, ipady=200, ipadx=320, sticky=E, padx=100)

        # Labels
        Label(self.savings_frame, text="Your savings", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=135, pady=23, ipadx=350, ipady=50) \

        ttk.Combobox(self.savings_frame, font=('Arial', 20), values=self.user_goals,
                     textvariable=self.current_goal) \
            .grid(row=1, column=0, sticky=W, padx=100, pady=40)

        Button(self.savings_frame, text="Submit", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.submit_open_goal()) \
            .grid(row=2, column=0, sticky=W, padx=100)

        Button(self.savings_frame, text="Delete", font=('Arial', 15), bg="light gray", width=10,
               command=lambda: self.controller.delete_goal()) \
            .grid(row=2, column=0, sticky=W, padx=305)

        Button(self.savings_frame, text="Make new goal", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.make_new_goal()) \
            .grid(row=3, column=0, sticky=W, padx=150, pady=60)

        Button(self.savings_frame, text="Investments", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.investments()) \
            .grid(row=4, column=0, sticky=W, padx=150)

        Button(self.savings_frame, text="Bank deposit", font=('Arial', 15), bg="light gray", width=20,
               command=lambda: self.controller.bank_deposit()) \
            .grid(row=5, column=0, sticky=W, padx=150, pady=30)

        Button(self.savings_frame, text="Back", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: self.controller.back()) \
            .grid(row=6, column=1, sticky=E, padx=20)

    def initial_overview(self):
        Label(self.overview_frame, text="Choose your goal").grid()

    def update_goal_list(self):
        ...

    def make_new_goal_window(self):
        self.make_goal_window = Toplevel(self.root, bg=self.bg_color)
        self.make_goal_window.geometry("400x200")
        self.make_goal_window.title("Make new goal")
        self.make_goal_window.resizable(False, False)

        # Goal name
        Label(self.make_goal_window, text="Goal name:", font=('Arial', 12)).grid(row=0, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15)).grid(row=1, column=0, padx=100, sticky=W)

        # Goal amount
        Label(self.make_goal_window, text="Goal amount:", font=('Arial', 12)).grid(row=2, column=0, padx=100, sticky=W)
        Entry(self.make_goal_window, font=('Arial', 15)).grid(row=3, column=0, padx=100, sticky=W)

        # Goal date
        Label(self.make_goal_window, text="Goal date:", font=('Arial', 12)).grid(row=4, column=0, padx=100, sticky=W)

        # DateEntry
        cal = DateEntry(self.make_goal_window, width=12, background='light gray', foreground='black', borderwidth=2,
                        date_pattern='yyyy-mm-dd', font=('Arial', 12))
        cal.grid(row=5, column=0, padx=145, sticky=W, pady=5)

        # Submit goal
        Button(self.make_goal_window, text="Submit goal", font=('Arial', 15), bg="light gray").grid(row=6, column=0,
                                                                                                    padx=150, sticky=W)

        # Focus on TopLevel window
        self.make_goal_window.grab_set()

    def destroy_savings_frame(self):
        self.savings_frame.destroy()

    def destroy_make_goal_window(self):
        self.make_goal_window.destroy()
