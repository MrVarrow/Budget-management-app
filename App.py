from tkinter import *
import tkinter
from tkinter import messagebox
import re
from email_validator import validate_email, EmailNotValidError
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class StartPage:
    def __init__(self):
        ...

    def create_root(self):
        self.root = Tk()
        self.root.configure(bg="light gray")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.title("Budget")
        self.main_menu(self.root)

    def main_menu(self, root):
        self.root = root
        self.show_password_icon = PhotoImage(file="hide.png")
        self.show_password_icon = self.show_password_icon.subsample(20, 20)

        self.main_menu_frame = Frame(self.root)
        self.main_menu_frame.grid(row=0, column=0, sticky=NSEW)

        Label(self.main_menu_frame, text="Login to your budget manager", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=80, pady=20, ipadx=220, ipady=50)

        Label(self.main_menu_frame, text="login:", font=('Arial', 20)) \
            .grid(row=1, column=0, padx=500, sticky=W)
        Entry(self.main_menu_frame, font=('Arial', 20)) \
            .grid(row=2, column=0, padx=500, sticky=W, pady=10)
        Label(self.main_menu_frame, text="password:", font=('Arial', 20)) \
            .grid(row=3, column=0, padx=500, sticky=W)
        self.password_entry = Entry(self.main_menu_frame, font=('Arial', 20), show="*")
        self.password_entry.grid(row=4, column=0, padx=500, sticky=W, pady=10)

        show_password_icon_widget = Button(self.main_menu_frame, text="S", bg='light gray',
                                           image=self.show_password_icon, command=self.show_password)
        show_password_icon_widget.image = self.show_password_icon
        show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)

        Button(self.main_menu_frame, text="Login", font=('Arial', 25), bg='light gray', command=self.login) \
            .grid(row=5, column=0, padx=580, sticky=W, pady=50, ipadx=20)
        Label(self.main_menu_frame, text="You don't have an account?", font=('Arial', 15)) \
            .grid(row=6, column=0, padx=530, sticky=W, pady=5)
        Button(self.main_menu_frame, text="Create account", font=('Arial', 15), bg='light gray',
               command=self.create_acc) \
            .grid(row=7, column=0)
        Button(self.main_menu_frame, text="Close", font=('Arial', 20), bg='light gray', command=self.exit_from_app) \
            .grid(row=8, column=0, sticky=SE, padx=40, ipadx=20, pady=20)

    def exit_from_app(self):
        result = tkinter.messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass

    def login(self):
        self.main_menu_frame.destroy()
        new_page = LoginUser(self.root)
        new_page.logged_user_page()

    def create_acc(self):
        self.main_menu_frame.destroy()
        new_page = CreateAccount(self.root)
        new_page.create_account_page()

    def show_password(self):
        show_password_icon_widget = Button(self.main_menu_frame, text="S", bg='light gray',
                                           image=self.show_password_icon, command=self.hide_password)
        show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)
        self.password_entry.config(show="")

    def hide_password(self):
        show_password_icon_widget = Button(self.main_menu_frame, text="S", bg='light gray',
                                           image=self.show_password_icon, command=self.show_password)
        show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)
        self.password_entry.config(show="*")


class CreateAccount:
    def __init__(self, root):
        self.root = root

    def create_account_page(self):
        self.create_acc_page = Frame(self.root)
        self.create_acc_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.create_acc_page, text="Create your account", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=100, pady=10, ipadx=310, ipady=50)
        Label(self.create_acc_page, text="login:", font=('Arial', 20)) \
            .grid(row=1, column=1, padx=450, sticky=W)

        self.login = Entry(self.create_acc_page, font=('Arial', 20))
        self.login.grid(row=2, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_acc_page, text="password:", font=('Arial', 20)) \
            .grid(row=3, column=1, padx=450, sticky=W)

        self.password = Entry(self.create_acc_page, font=('Arial', 20))
        self.password.grid(row=4, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_acc_page, text="repeat password:", font=('Arial', 20)) \
            .grid(row=5, column=1, padx=450, sticky=W)

        self.repeat_password = Entry(self.create_acc_page, font=('Arial', 20))
        self.repeat_password.grid(row=6, column=1, padx=450, sticky=W, pady=10)

        Label(self.create_acc_page, text="e-mail:", font=('Arial', 20)) \
            .grid(row=7, column=1, padx=450, sticky=W)

        self.email = Entry(self.create_acc_page, font=('Arial', 20))
        self.email.grid(row=8, column=1, padx=450, sticky=W, pady=10)

        Button(self.create_acc_page, text="create account", font=('Arial', 25), bg="light gray",
               command=self.create_acc) \
            .grid(row=9, column=1, pady=10)
        Button(self.create_acc_page, text="Back", font=('Arial', 20), bg="light gray",
               command=self.exit_from_create_acc) \
            .grid(row=10, column=1, pady=10, ipadx=20, sticky=E, padx=5)
        Label(self.create_acc_page, font=('Arial', 12), borderwidth=2, text="How should login look:\n"
                                                                            "-at least 6 characters\n"
                                                                            "How should password look:\n"
                                                                            "-at least 8 characters\n"
                                                                            "-at least one big letter\n"
                                                                            "-at least one small letter\n"
                                                                            "-at least one number\n"
                                                                            "-at least one special character except _",
              relief="solid") \
            .grid(row=3, column=1, rowspan=7, sticky=NW, padx=120, pady=45, ipadx=20, ipady=20)
        Label(self.create_acc_page, font=('Arial', 12), borderwidth=2, relief="solid", text="password strength:\n"
                                                                                            "-----------------\n"
                                                                                            "strong") \
            .grid(row=4, column=1, rowspan=3, columnspan=2, sticky=SE, padx=300, pady=25, ipadx=20, ipady=20)
        self.notification_email_state = BooleanVar()
        Checkbutton(self.create_acc_page, text="I want to get e-mail notifications about news", font=('Arial', 12),
                    variable=self.notification_email_state, onvalue=True, offvalue=False) \
            .grid(row=8, column=1, columnspan=2, sticky=E, padx=150)

    def create_acc(self):
        # sending email is working but added temp as comments to avoid spam while testing app
        if self.check_login_requirements() and \
                self.check_password_requirements() and \
                self.check_if_passwords_are_the_same() and \
                self.email_validate(self.email.get()):

            # self.send_confirm_email()

            # Add user to database of users with wants e-mails if selected
            if self.notification_email_state.get():
                pass  # Add user to database(later)

            # Go back to login
            self.back_to_login()

    def check_login_requirements(self):
        if not len(self.login.get()) >= 6:
            messagebox.showerror(title='Error', message="Your login is too short.")
            return False
        # check if there is the same login in database(later)
        return True

    def send_email(self, sender_email, sender_password, receiver_email, subject, message):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)  # You can omit this line
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")
        finally:
            server.quit()

    def send_confirm_email(self):
        sender_email = 'budgetappofficial@gmail.com'
        sender_password = ''  # for safety reasons leaving empty
        receiver_email = '{}'.format(self.email.get())
        subject = 'Thanks for Registration!'
        message = 'Your Registration to BudgetApp went successfully, now you can login to your account.'

        self.send_email(sender_email, sender_password, receiver_email, subject, message)

    def email_validate(self, email):
        try:
            v = validate_email(email)
            email = v.normalized
            return True
        except EmailNotValidError as e:
            messagebox.showerror(title='Error', message=str(e))
            return False

    def check_password_requirements(self):
        if len(self.password.get()) < 8:
            messagebox.showerror(title='Error', message="Your password is too short.")
            return False
        if not re.search("[a-z]", self.password.get()):
            messagebox.showerror(title='Error', message="Your password is missing small letter.")
            return False
        if not re.search("[A-Z]", self.password.get()):
            messagebox.showerror(title='Error', message="Your password is missing large letter.")
            return False
        if not re.search("[0-9]", self.password.get()):
            messagebox.showerror(title='Error', message="Your password is missing digit.")
            return False
        if not re.search(r"\W", self.password.get()):
            messagebox.showerror(title='Error', message="Your password is missing special character.")
            return False
        return True

    def check_if_passwords_are_the_same(self):
        if not self.password.get() == self.repeat_password.get():
            messagebox.showerror(title='Error', message="Passwords are not the same")
            return False
        return True

    def back_to_login(self):
        self.create_acc_page.destroy()
        login_page = StartPage()
        login_page.main_menu(self.root)
        tkinter.messagebox.showinfo(title="Information", message="Your account has been created, now you can login")

    def exit_from_create_acc(self):
        result = tkinter.messagebox.askquestion(title='Warning', message="Do you want back to login page?")
        if result == "yes":
            self.create_acc_page.destroy()
            login_page = StartPage()
            login_page.main_menu(self.root)
        elif result == "no":
            pass


class LoginUser:
    def __init__(self, root):
        self.root = root
        self.acc_icon = PhotoImage(file="user.png")
        self.acc_icon = self.acc_icon.subsample(20, 20)
        self.settings_icon = PhotoImage(file="gear.png")
        self.settings_icon = self.settings_icon.subsample(20, 20)

    def logged_user_page(self):
        self.logged_usr_page = Frame(self.root)
        self.logged_usr_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.logged_usr_page, text="Main page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)
        Button(self.logged_usr_page, text="Manage budget", font=('Arial', 20), bg='light gray', width=15,
               command=self.manage_budget) \
            .grid(row=1, column=0, pady=20)
        Button(self.logged_usr_page, text="Statistics", font=('Arial', 20), bg='light gray', width=15,
               command=self.stats) \
            .grid(row=2, column=0, pady=20)
        Button(self.logged_usr_page, text="Shopping list", font=('Arial', 20), bg='light gray', width=15,
               command=self.shopping_list) \
            .grid(row=3, column=0, pady=20)
        Button(self.logged_usr_page, text="Savings", font=('Arial', 20), bg='light gray', width=15,
               command=self.savings) \
            .grid(row=1, column=1, pady=20)
        Button(self.logged_usr_page, text="Receipts", font=('Arial', 20), bg='light gray', width=15,
               command=self.receipts) \
            .grid(row=2, column=1, pady=20)
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 20), bg='light gray', width=15,
               command=self.rate_us) \
            .grid(row=3, column=1, pady=20)
        Button(self.logged_usr_page, text="Mobile app", font=('Arial', 20), bg='light gray', width=15,
               command=self.mobile_app) \
            .grid(row=4, column=0, columnspan=2, pady=65)
        Button(self.logged_usr_page, text="Logout", font=('Arial', 20), bg='light gray', command=self.logout) \
            .grid(row=4, column=2, sticky=NE, padx=20, pady=50, ipadx=10)
        Button(self.logged_usr_page, text="Exit", font=('Arial', 20), bg='light gray', command=self.exit) \
            .grid(row=4, column=2, sticky=SE, padx=20, pady=10, ipadx=30)

        acc_icon_widget = Button(self.logged_usr_page, text="A", bg='light gray', image=self.acc_icon, command=self.settings_command)
        acc_icon_widget.image = self.acc_icon
        acc_icon_widget.grid(row=0, column=2, sticky=NE, padx=20, pady=10)

        settings_icon_widget = Button(self.logged_usr_page, text="S", bg='light gray', image=self.settings_icon, command=self.your_acc)
        settings_icon_widget.image = self.settings_icon
        settings_icon_widget.grid(row=0, column=2, sticky=NW, padx=30, pady=10)

    def settings_command(self):
        self.logged_usr_page.destroy()
        settings = Settings(self.root)
        settings.settings_layout()

    def your_acc(self):
        self.logged_usr_page.destroy()
        your_acc = Account(self.root)
        your_acc.account_layout()

    def manage_budget(self):
        self.logged_usr_page.destroy()
        manage_budget = ManageBudget(self.root)
        manage_budget.manage_budget_layout()

    def stats(self):
        self.logged_usr_page.destroy()
        statistics = Statistics(self.root)
        statistics.statistics_layout()

    def shopping_list(self):
        self.logged_usr_page.destroy()
        shopping_list = ShoppingList(self.root)
        shopping_list.shopping_list_layout()

    def savings(self):
        self.logged_usr_page.destroy()
        savings = Savings(self.root)
        savings.savings_layout()

    def receipts(self):
        self.logged_usr_page.destroy()
        receipts = Receipts(self.root)
        receipts.receipts_layout()

    def rate_us(self):
        rate_us = RateUs(self.root)
        rate_us.rate_us_layout()

    def mobile_app(self):
        mobile_app = MobileApp(self.root)
        mobile_app.mobile_app_layout()

    def logout(self):
        result = tkinter.messagebox.askquestion(title='Warning', message="Do you want to logout from Budget manager?")
        if result == "yes":
            self.logged_usr_page.destroy()
            login_page = StartPage()
            login_page.main_menu(self.root)
        elif result == "no":
            pass

    def exit(self):
        result = tkinter.messagebox.askquestion(title='Warning', message="Do you want to close Budget manager?")
        if result == "yes":
            self.root.destroy()
        elif result == "no":
            pass

    def exit_to_logged_user_page(self, frame):
        frame.destroy()
        self.logged_user_page()


class Receipts:
    def __init__(self, root):
        self.root = root

    def receipts_layout(self):
        ...


class Savings:
    def __init__(self, root):
        self.root = root

    def savings_layout(self):
        ...


class ShoppingList:
    def __init__(self, root):
        self.root = root

    def shopping_list_layout(self):
        ...


class Statistics:
    def __init__(self, root):
        self.root = root

    def statistics_layout(self):
        ...


class ManageBudget:
    def __init__(self, root):
        self.root = root

    def manage_budget_layout(self):
        ...


class MobileApp:
    def __init__(self, root):
        self.root = root
        self.copy_icon = PhotoImage(file="copy.png")
        self.copy_icon = self.copy_icon.subsample(20, 20)

    def mobile_app_layout(self):
        self.mobile_app_root = Toplevel(self.root)
        self.mobile_app_root.geometry("400x200")
        self.mobile_app_root.title("Download our mobile app")

        Label(self.mobile_app_root, text="There is a link to our mobile app:\n"
                                         "Link", font=('Arial', 15)) \
            .grid(row=0, column=0, pady=10)
        Label(self.mobile_app_root, text="To download you have to click this link on your mobile device,\n"
                                         "so type it in google\n"
                                         "or copy and sent it to yourself then use on phone", borderwidth=2,
              relief="solid") \
            .grid(row=1, column=0, pady=15, padx=30)
        copy_icon_widget = Button(self.mobile_app_root, text="copy", image=self.copy_icon, bg="light gray")
        copy_icon_widget.image = self.copy_icon
        copy_icon_widget.grid(row=0, column=0, rowspan=2, sticky=NE, padx=10, pady=40)
        Button(self.mobile_app_root, text="Close", font=('Arial', 15), command=self.mobile_app_root.destroy,
               bg="light gray") \
            .grid(row=2, column=0)

        self.mobile_app_root.grab_set()

    def copy_app_link(self):
        ...


class RateUs:
    def __init__(self, root):
        self.root = root
        self.empty_star = PhotoImage(file="empty_star.png")
        self.empty_star = self.empty_star.subsample(20, 20)
        self.full_star = PhotoImage(file="full_star.png")
        self.full_star = self.full_star.subsample(20, 20)
        self.star_list = ["1", "2", "3", "4", "5"]
        self.final_rating = ""

    def rate_us_layout(self):
        self.rate_us_root = Toplevel(self.root)
        self.rate_us_root.geometry("400x200")
        self.rate_us_root.title("Rate us!")
        Label(self.rate_us_root, text="Rate our app!", font=('Arial', 15)).grid(row=0, column=0, padx=135, pady=15,
                                                                                sticky=W)

        i = 100
        for star in self.star_list:
            Button(self.rate_us_root, image=self.empty_star, bg="light gray",
                   command=lambda user_rating=star: self.fill_stars(user_rating)) \
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40

        self.user_rate_widget = Label(self.rate_us_root, text="Your rating:\n", font=('Arial', 12))
        self.user_rate_widget.grid(row=2, column=0, sticky=W, padx=150, pady=10)

        Button(self.rate_us_root, text="Submit", font=('Arial', 15), width=7, bg="light gray",
               command=self.submit_rating).grid(row=3, column=0, sticky=W, padx=150)

        self.rate_us_root.grab_set()

    def submit_rating(self):
        #sent final rating to me, maybe to database to create some statistic
        print(self.final_rating)
        self.rate_us_root.destroy()

    def fill_stars(self, user_rating):
    #maybe optimize with stars widget in frame so you can delete frame and create new one with no stacking button on top of each other
    #in future add check if user rate us, limit one per acc with ability to change your rating
        filled_star_list = []
        unfilled_star_list = []
        for i in range(0, int(user_rating)):
            x = self.star_list[i]
            filled_star_list.append(x)

        for item in range(int(user_rating), len(self.star_list)):
            x = self.star_list[item]
            unfilled_star_list.append(x)

        i = 100
        for star in filled_star_list:
            Button(self.rate_us_root, image=self.full_star, bg="light gray", command=lambda user_rating=star: self.fill_stars(user_rating))\
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40
        for star in unfilled_star_list:
            Button(self.rate_us_root, image=self.empty_star, bg="light gray",
                   command=lambda user_rating=star: self.fill_stars(user_rating)) \
                .grid(row=1, column=0, padx=i, sticky=W)
            i += 40
        self.user_rate_widget.configure(text="Your rating:\n {} star".format(user_rating))
        self.final_rating = user_rating


class Account:
    def __init__(self, root):
        self.root = root
        self.exit_method = LoginUser(self.root)

    def account_layout(self):
        self.acc_page = Frame(self.root)
        self.acc_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.acc_page, text="Your account")
        Button(self.acc_page, text="Change password").grid()
        Button(self.acc_page, text="Verify e-mail").grid()
        Button(self.acc_page, text="Change e-mail").grid()
        Button(self.acc_page, text="Change e-mail notification settings").grid()
        Button(self.acc_page, text="delete account")\
            .grid()
        Button(self.acc_page, text="clear all data")\
            .grid()
        Button(self.acc_page, text="Close", command=lambda frame=self.acc_page: self.exit_method.exit_to_logged_user_page(frame)).grid()

    def change_password(self):
        ...

    def verify_email(self):
        ...

    def change_email(self):
        ...

    def change_email_notifications(self):
        ...

    def delete_data(self):
        ...

    def clear_all_data(self):
        ...


class Settings:
    def __init__(self, root):
        self.root = root
        self.exit_method = LoginUser(self.root)

    def settings_layout(self):
        self.settings_page = Frame(self.root)
        self.settings_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.settings_page, text="Settings").grid()
        Checkbutton(self.settings_page, text="Dark mode").grid()
        Button(self.settings_page, text="Support and Help").grid()
        Button(self.settings_page, text="App version").grid()
        Button(self.settings_page, text="Credits").grid()
        Button(self.settings_page, text="About app").grid()
        Button(self.settings_page, text="Close",
               command=lambda frame=self.settings_page: self.exit_method.exit_to_logged_user_page(frame)).grid()

    def support_and_help(self):
        ...

    def app_version(self):
        ...

    def credits(self):
        ...

    def about_app(self):
        ...

    def dark_mode(self):
        ...


def main():
    run_app = StartPage()
    run_app.create_root()
    mainloop()


if __name__ == '__main__':
    main()
