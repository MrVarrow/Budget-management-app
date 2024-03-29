from tkinter import *


class AccountPageView:
    def __init__(self, master, controller):
        self.controller = controller
        self.root = master

        # Frame creation
        self.acc_page = Frame(master)
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
               command=lambda: self.account_frame_destroy())\
            .grid(row=4, column=0, sticky=SE, padx=40, pady=50, ipady=5)

    # Destroy frame
    def account_frame_destroy(self):
        self.acc_page.destroy()

    def verify_email_window(self, user_email):
        # Creating e-mail verification window
        self.verify_email_root = Toplevel(self.root)
        self.verify_email_root.geometry("400x200")
        self.verify_email_root.title("E-mail verification")

        # Label
        Label(self.verify_email_root, text="To verify e-mail enter the code, that was send on your email:\n"
                                           "{}"
                                           "note: if you close this window you will need new code.".format(user_email))\
            .grid(row=0, column=0)

        # Code Entry
        self.code_entry = Entry(self.verify_email_root)
        self.code_entry.grid(row=1, column=0)

        # Resend e-mail button
        Button(self.verify_email_root, text="Resend e-mail", command=lambda: self.controller.send_email()) \
            .grid(row=1, column=0, sticky=E)

        # Submit code button
        Button(self.verify_email_root, text="Submit code",
               command=lambda: self.controller.submit_verification_code(self.code_entry.get())) \
            .grid(row=2, column=0)

        # Focus on e-mail verification window
        self.verify_email_root.grab_set()

    # Destroy verify email root destroy
    def verify_email_root_destroy(self):
        self.verify_email_root.destroy()

    def change_password_window(self):
        # Creating password change window
        self.change_password_root = Toplevel(self.root)
        self.change_password_root.geometry("400x200")
        self.change_password_root.title("Password change")

        # Labels and entries
        Label(self.change_password_root, text="Old password:") \
            .grid(row=0, column=0)
        self.old_password_entry = Entry(self.change_password_root)
        self.old_password_entry.grid(row=1, column=0)

        Label(self.change_password_root, text="New password:") \
            .grid(row=2, column=0)
        self.new_password_entry = Entry(self.change_password_root)
        self.new_password_entry.grid(row=3, column=0)

        Label(self.change_password_root, text="Repeat new password:") \
            .grid(row=4, column=0)
        self.new_password_reentry = Entry(self.change_password_root)
        self.new_password_reentry.grid(row=5, column=0)

        # Submit password button
        Button(self.change_password_root, text="Submit password",
               command=lambda: self.controller.submit_password(self.old_password_entry.get(),
                                                               self.new_password_entry.get(),
                                                               self.new_password_reentry.get())) \
            .grid(row=6, column=0)

        # Focus on password change window
        self.change_password_root.grab_set()

    def change_password_window_destroy(self):
        self.change_password_root.destroy()

    def change_email_window(self):
        # Creating e-mail change window
        self.change_email_root = Toplevel(self.root)
        self.change_email_root.geometry("400x200")
        self.change_email_root.title("E-mail change")

        # Labels and entries
        Label(self.change_email_root, text="Old e-mail:") \
            .grid(row=0, column=0)
        self.old_email_entry = Entry(self.change_email_root)
        self.old_email_entry.grid(row=1, column=0)

        Label(self.change_email_root, text="New e-mail:") \
            .grid(row=2, column=0)
        self.new_email_entry = Entry(self.change_email_root)
        self.new_email_entry.grid(row=3, column=0)

        Label(self.change_email_root, text="Repeat new e-mail:") \
            .grid(row=4, column=0)
        self.new_email_reentry = Entry(self.change_email_root)
        self.new_email_reentry.grid(row=5, column=0)

        # Submit E-mail button
        Button(self.change_email_root, text="Submit e-mail",
               command=lambda: self.controller.submit_email(self.old_email_entry.get(), self.new_email_entry.get(),
                                                            self.new_email_reentry.get())) \
            .grid(row=6, column=0)

        # Focus on change e-mail window
        self.change_email_root.grab_set()

    def change_email_window_destroy(self):
        self.change_email_root.destroy()
