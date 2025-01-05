from tkinter import *


class LoggedUserPageView:
    def __init__(self, master, controller, bg_color):
        self.bg_color = bg_color
        self.controller = controller

        # Loading icons and scaling them
        self.acc_icon = PhotoImage(file="Icons/user.png")
        self.acc_icon = self.acc_icon.subsample(20, 20)
        self.settings_icon = PhotoImage(file="Icons/gear.png")
        self.settings_icon = self.settings_icon.subsample(20, 20)

        # Frame creation
        self.logged_usr_page = Frame(master, bg=self.bg_color)
        self.logged_usr_page.grid(row=0, column=0, sticky=NSEW)

        # Labels
        Label(self.logged_usr_page, text="Main page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)

        # Manage budget button
        Button(self.logged_usr_page, text="Manage budget", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.manage_budget) \
            .grid(row=1, column=0, pady=20)

        # Statistics button
        Button(self.logged_usr_page, text="Statistics", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.stats) \
            .grid(row=2, column=0, pady=20)

        # Shopping list button
        Button(self.logged_usr_page, text="Shopping list", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.shopping_list) \
            .grid(row=3, column=0, pady=20)

        # Savings button
        Button(self.logged_usr_page, text="Savings", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.savings) \
            .grid(row=1, column=1, pady=20)

        # Receipts button
        Button(self.logged_usr_page, text="Receipts", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.receipts) \
            .grid(row=2, column=1, pady=20)

        # Rate us button
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.rate_us) \
            .grid(row=3, column=1, pady=20)

        # Mobile app button
        Button(self.logged_usr_page, text="Questionnaire", font=('Arial', 20), bg='light gray', width=15,
               command=self.controller.questionnaire) \
            .grid(row=4, column=0, columnspan=2, pady=65)

        # Logout button
        Button(self.logged_usr_page, text="Logout", font=('Arial', 20), bg='light gray',
               command=self.controller.logout) \
            .grid(row=4, column=2, sticky=NE, padx=20, pady=50, ipadx=10)

        # Exit button
        Button(self.logged_usr_page, text="Exit", font=('Arial', 20), bg='light gray', command=self.controller.exit) \
            .grid(row=4, column=2, sticky=SE, padx=20, pady=10, ipadx=30)

        # Account button
        acc_icon_widget = Button(self.logged_usr_page, text="A", bg='light gray', image=self.acc_icon,
                                 command=self.controller.your_acc)
        acc_icon_widget.image = self.acc_icon
        acc_icon_widget.grid(row=0, column=2, sticky=NE, padx=20, pady=10)

        # Settings button
        settings_icon_widget = Button(self.logged_usr_page, text="S", bg='light gray', image=self.settings_icon,
                                      command=self.controller.settings)
        settings_icon_widget.image = self.settings_icon
        settings_icon_widget.grid(row=0, column=2, sticky=NW, padx=30, pady=10)

    # Destroying frame
    def destroy_logged_user_frame(self):
        self.logged_usr_page.destroy()
