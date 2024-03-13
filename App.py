import requests
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk
import re


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

        Button(self.create_acc_page, text="create account", font=('Arial', 25), bg="light gray", command=self.create_acc) \
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
        Checkbutton(self.create_acc_page, text="I want to get e-mail notifications about news", font=('Arial', 12)) \
            .grid(row=8, column=1, columnspan=2, sticky=E, padx=150)

    def create_acc(self):
        if len(self.login.get()) < 6:
            messagebox.showerror(title='Error', message="Your login is too short.")

        else:
            if self.check_password_requirements():
                print("yes")

                if self.check_if_passwords_are_the_same():
                    print("same")
                    self.email_validate()
                else:
                    messagebox.showerror(title='Error', message="Passwords are not the same")

            else:
                pass
        # check if login is correct- done
        # check if there is the same login in database(later)
        # check if password meets requirements - done
        # check if passwords are the same -d done
        # check if e-mail is correct
        # check if user chcecked the check button to recive e-mails
        # send user an e-mail with information "you are succesfully registered"
        ...

    def email_validate(self):
        #to fix
        email_address = str(self.email.get())
        response = requests.get(
            "https://verifalia.com/validate-email",
            params={'email': email_address})

        status = response.json()['status']
        if status == "valid":
            print("email is valid")
        elif status == "invalid":
            print("email is invalid")
        else:
            print("email was unknown")

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
            return False
        return True

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

    def logged_user_page(self):
        self.acc_icon = PhotoImage(file="user.png")
        self.acc_icon = self.acc_icon.subsample(20, 20)
        self.settings_icon = PhotoImage(file="gear.png")
        self.settings_icon = self.settings_icon.subsample(20, 20)

        self.logged_usr_page = Frame(self.root)
        self.logged_usr_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.logged_usr_page, text="Main page", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)
        Button(self.logged_usr_page, text="Manage budget", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=1, column=0, pady=20)
        Button(self.logged_usr_page, text="Statistics", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=2, column=0, pady=20)
        Button(self.logged_usr_page, text="Shopping list", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=3, column=0, pady=20)
        Button(self.logged_usr_page, text="Savings", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=1, column=1, pady=20)
        Button(self.logged_usr_page, text="Receipts", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=2, column=1, pady=20)
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=3, column=1, pady=20)
        Button(self.logged_usr_page, text="Mobile app", font=('Arial', 20), bg='light gray', width=15) \
            .grid(row=4, column=0, columnspan=2, pady=65)
        Button(self.logged_usr_page, text="Logout", font=('Arial', 20), bg='light gray', command=self.logout) \
            .grid(row=4, column=2, sticky=NE, padx=20, pady=50, ipadx=10)
        Button(self.logged_usr_page, text="Exit", font=('Arial', 20), bg='light gray', command=self.exit) \
            .grid(row=4, column=2, sticky=SE, padx=20, pady=10, ipadx=30)

        acc_icon_widget = Button(self.logged_usr_page, text="A", bg='light gray', image=self.acc_icon)
        acc_icon_widget.image = self.acc_icon
        acc_icon_widget.grid(row=0, column=2, sticky=NE, padx=20, pady=10)

        settings_icon_widget = Button(self.logged_usr_page, text="S", bg='light gray', image=self.settings_icon)
        settings_icon_widget.image = self.settings_icon
        settings_icon_widget.grid(row=0, column=2, sticky=NW, padx=30, pady=10)

    def settings(self):
        ...

    def your_acc(self):
        ...

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

    def manage_budget(self):
        ...

    def stats(self):
        ...

    def shopping_list(self):
        ...

    def savings(self):
        ...

    def receipts(self):
        ...

    def rate_us(self):
        ...

    def mobile_app(self):
        ...


def main():
    run_app = StartPage()
    run_app.create_root()
    mainloop()


if __name__ == '__main__':
    main()
