from tkinter import *


class AccountPageView:
    def __init__(self, master, controller, bg_color):
        self.bg_color = bg_color
        self.controller = controller
        self.root = master
        # Icon get
        self.send_email_icon = PhotoImage(file="Icons/email.png")
        self.send_email_icon = self.send_email_icon.subsample(20, 20)
        # Variables for entries
        self.old_email_entry = StringVar()
        self.new_email_entry = StringVar()
        self.new_email_reentry = StringVar()
        self.old_password_entry = StringVar()
        self.new_password_entry = StringVar()
        self.new_password_reentry = StringVar()
        self.code_entry = StringVar()

        # Frame creation
        self.acc_page = Frame(master, bg=self.bg_color)
        self.acc_page.grid(row=0, column=0, sticky=NSEW)

        # Labels
        Label(self.acc_page, text="Your account", font=('Arial', 40), bg="light gray")\
            .grid(row=0, column=0, sticky=EW, padx=280, pady=20, ipadx=220, ipady=50)

        # Change password button
        Button(self.acc_page, text="Change password", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.change_password())\
            .grid(row=1, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # Verify e-mail button
        Button(self.acc_page, text="Verify e-mail", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.verify_email())\
            .grid(row=1, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Change e-mail button
        Button(self.acc_page, text="Change e-mail", font=('Arial', 20), width=15, bg="light gray", command=lambda: controller.change_email()) \
            .grid(row=2, column=0, sticky=W, padx=200, pady=30, ipady=5)

        # Change e-mail notification settings button
        Button(self.acc_page, text="Change e-mail notification settings", font=('Arial', 15), width=22, bg="light gray",
               height=2, wraplength=250, command=lambda: controller.change_email_notifications())\
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
               command=lambda: self.controller.back_from_acc_page())\
            .grid(row=4, column=0, sticky=SE, padx=40, pady=50, ipady=5)

    # Destroy frame
    def account_frame_destroy(self):
        self.acc_page.destroy()

    # Creating e-mail verification window
    def verify_email_window(self, user_email):
        self.verify_email_root = Toplevel(self.root, bg=self.bg_color)
        self.verify_email_root.geometry("400x200")
        self.verify_email_root.title("E-mail verification")
        self.verify_email_root.resizable(False, False)

        # Label
        Label(self.verify_email_root, text="To verify e-mail enter the code, that was send on your email:\n"
                                           "{}\n"
                                           "note: if you close this window you will need new code.".format(user_email),
              bd=2, relief="solid")\
            .grid(row=0, column=0, padx=40, pady=20)

        # Code Entry
        Entry(self.verify_email_root, font=('Arial', 15), textvariable=self.code_entry) \
            .grid(row=1, column=0, padx=80)

        # Resend e-mail button
        Button(self.verify_email_root, image=self.send_email_icon, bg="light gray", font=('Arial', 15), command=lambda: self.controller.send_email()) \
            .grid(row=1, column=0, sticky=E, padx=30)

        # Submit code button
        Button(self.verify_email_root, text="Submit code", bg="light gray", font=('Arial', 15),
               command=lambda: self.controller.submit_verification_code(self.code_entry.get())) \
            .grid(row=2, column=0, pady=20)

        # Focus on e-mail verification window
        self.verify_email_root.grab_set()

    # Destroy verify email root destroy
    def verify_email_root_destroy(self):
        self.verify_email_root.destroy()

    # Creating password change window
    def change_password_window(self):
        self.change_password_root = Toplevel(self.root, bg=self.bg_color)
        self.change_password_root.geometry("400x200")
        self.change_password_root.title("Password change")
        self.change_password_root.resizable(False, False)

        # Labels and entries
        Label(self.change_password_root, text="Old password:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=0, column=0, sticky=W, padx=90)
        Entry(self.change_password_root, font=('Arial', 15), textvariable=self.old_password_entry) \
            .grid(row=1, column=0, padx=90)

        Label(self.change_password_root, text="New password:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=2, column=0, sticky=W, padx=90)
        Entry(self.change_password_root, font=('Arial', 15), textvariable=self.new_password_entry) \
            .grid(row=3, column=0, padx=90)

        Label(self.change_password_root, text="Repeat new password:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=4, column=0, sticky=W, padx=90)
        Entry(self.change_password_root, font=('Arial', 15), textvariable=self.new_password_reentry) \
            .grid(row=5, column=0, padx=90)

        # Submit password button
        Button(self.change_password_root, text="Submit password", font=('Arial', 15), bg="light grey",
               command=lambda: self.controller.submit_password(self.old_password_entry.get(),
                                                               self.new_password_entry.get(),
                                                               self.new_password_reentry.get())) \
            .grid(row=6, column=0, pady=5)

        # Focus on password change window
        self.change_password_root.grab_set()

    # Change password window destroy
    def change_password_window_destroy(self):
        self.change_password_root.destroy()

    # Creating e-mail change window
    def change_email_window(self):
        self.change_email_root = Toplevel(self.root, bg=self.bg_color)
        self.change_email_root.geometry("400x200")
        self.change_email_root.title("E-mail change")
        self.change_email_root.resizable(False, False)

        # Labels and entries
        Label(self.change_email_root, text="Old e-mail:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=0, column=0, sticky=W, padx=90)
        Entry(self.change_email_root, font=('Arial', 15), textvariable=self.old_email_entry) \
            .grid(row=1, column=0, sticky=W, padx=90)

        Label(self.change_email_root, text="New e-mail:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=2, column=0, sticky=W, padx=90)
        Entry(self.change_email_root, font=('Arial', 15), textvariable=self.new_email_entry) \
            .grid(row=3, column=0, sticky=W, padx=90)

        Label(self.change_email_root, text="Repeat new e-mail:", font=('Arial', 10), bg=self.bg_color) \
            .grid(row=4, column=0, sticky=W, padx=90)
        Entry(self.change_email_root, font=('Arial', 15), textvariable=self.new_email_reentry) \
            .grid(row=5, column=0, sticky=W, padx=90)

        # Submit E-mail button
        Button(self.change_email_root, text="Submit e-mail", font=('Arial', 15), bg="light grey",
               command=lambda: self.controller.submit_email(self.old_email_entry.get(), self.new_email_entry.get(),
                                                            self.new_email_reentry.get())) \
            .grid(row=6, column=0, pady=5)

        # Focus on change e-mail window
        self.change_email_root.grab_set()

    # Change e-mail window destroy
    def change_email_window_destroy(self):
        self.change_email_root.destroy()
