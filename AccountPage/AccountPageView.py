from tkinter import *


class AccountPageView:
    def __init__(self, master, controller):
        self.controller = controller

        # Frame creation
        self.acc_page = Frame(master)
        self.acc_page.grid(row=0, column=0, sticky=NSEW)

        # Labels
        Label(self.acc_page, text="Your account", font=('Arial', 40), bg="light gray")\
            .grid(row=0, column=0, sticky=EW, padx=280, pady=20, ipadx=220, ipady=50)

        # Change password button
        Button(self.acc_page, text="Change password", font=('Arial', 20), width=15, bg="light gray")\
            .grid(row=1, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # Verify e-mail button
        Button(self.acc_page, text="Verify e-mail", font=('Arial', 20), width=15, bg="light gray")\
            .grid(row=1, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Change e-mail button
        Button(self.acc_page, text="Change e-mail", font=('Arial', 20), width=15, bg="light gray")\
            .grid(row=2, column=0, sticky=W, padx=200, pady=30, ipady=5)

        # Change e-mail notification settings button
        Button(self.acc_page, text="Change e-mail notification settings", font=('Arial', 15), width=22, bg="light gray",
               height=2, wraplength=250)\
            .grid(row=2, column=0, sticky=E, padx=200, pady=30, ipady=5)

        # Delete account button
        Button(self.acc_page, text="delete account", font=('Arial', 20), width=15, bg="light gray", fg="red",
               command=lambda: controller.delete_account()) \
            .grid(row=3, column=0, sticky=W, padx=200, pady=30, ipady=5)

        # Clear all data button
        Button(self.acc_page, text="clear all data", font=('Arial', 20), width=15, bg="light gray", fg="red",
               command=lambda: controller.clear_all_data()) \
            .grid(row=3, column=0, sticky=E, padx=200, pady=30, ipady=5)

        # Close button
        Button(self.acc_page, text="Close", font=('Arial', 15), width=8, bg="light gray",
               command=lambda: self.account_frame_destroy())\
            .grid(row=4, column=0, sticky=SE, padx=40, pady=50, ipady=5)

    # Destroy frame
    def account_frame_destroy(self):
        self.acc_page.destroy()
