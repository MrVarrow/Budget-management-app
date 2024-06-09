from tkinter import *


class CreateAccountPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.root = master
        self.bg_color = bg_color

        # Define variables for entries and checkbutton
        self.email_notification_state = BooleanVar()
        self.login_var = StringVar()
        self.password_var = StringVar()
        self.repeat_password_var = StringVar()
        self.email_var = StringVar()

        # Frame creation
        self.create_account_page = Frame(self.root, bg=self.bg_color)
        self.create_account_page.grid(row=0, column=0, sticky=NSEW)

        # Labels and Entries
        Label(self.create_account_page, text="Create your account", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=100, pady=10, ipadx=310, ipady=50)

        Label(self.create_account_page, font=('Arial', 12), borderwidth=2, text="How should login look:\n"
                                                                                "-at least 6 characters\n"
                                                                                "How should password look:\n"
                                                                                "-at least 8 characters\n"
                                                                                "-at least one big letter\n"
                                                                                "-at least one small letter\n"
                                                                                "-at least one number\n"
                                                                                "-at least one special character "
                                                                                "except _",
              relief="solid") \
            .grid(row=3, column=1, rowspan=7, sticky=NW, padx=120, pady=45, ipadx=20, ipady=20)
        Label(self.create_account_page, font=('Arial', 12), borderwidth=2, relief="solid", text="password strength:\n"
                                                                                                "-----------------\n"
                                                                                                "strong") \
            .grid(row=4, column=1, rowspan=3, columnspan=2, sticky=SE, padx=300, pady=25, ipadx=20, ipady=20)

        Label(self.create_account_page, text="login:", font=('Arial', 20), bg=self.bg_color) \
            .grid(row=1, column=1, padx=450, sticky=W)
        Entry(self.create_account_page, font=('Arial', 20), textvariable=self.login_var) \
            .grid(row=2, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_account_page, text="password:", font=('Arial', 20), bg=self.bg_color) \
            .grid(row=3, column=1, padx=450, sticky=W)
        Entry(self.create_account_page, font=('Arial', 20), textvariable=self.password_var) \
            .grid(row=4, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_account_page, text="repeat password:", font=('Arial', 20), bg=self.bg_color) \
            .grid(row=5, column=1, padx=450, sticky=W)
        Entry(self.create_account_page, font=('Arial', 20), textvariable=self.repeat_password_var) \
            .grid(row=6, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_account_page, text="e-mail:", font=('Arial', 20), bg=self.bg_color) \
            .grid(row=7, column=1, padx=450, sticky=W)
        Entry(self.create_account_page, font=('Arial', 20), textvariable=self.email_var) \
            .grid(row=8, column=1, padx=450, sticky=W, pady=10)

        # E-mail notifications checkbutton
        Checkbutton(self.create_account_page, text="I want to get e-mail notifications about news", font=('Arial', 12),
                    variable=self.email_notification_state, onvalue=True, offvalue=False, bg=self.bg_color,
                    command=lambda: self.controller.dark_mode()) \
            .grid(row=8, column=1, columnspan=2, sticky=E, padx=150)

        # Create account button
        Button(self.create_account_page, text="create account", font=('Arial', 25), bg="light gray",
               command=lambda: controller.create_account(self.login_var.get(), self.password_var.get(),
                                                         self.repeat_password_var.get(), self.email_var.get(),
                                                         self.email_notification_state.get())) \
            .grid(row=9, column=1, pady=10)

        # Back button
        Button(self.create_account_page, text="Back", font=('Arial', 20), bg="light gray",
               command=lambda: controller.back()) \
            .grid(row=10, column=1, pady=10, ipadx=20, sticky=E, padx=5)

    # Destroying frame
    def destroy_create_account_frame(self):
        self.create_account_page.destroy()
