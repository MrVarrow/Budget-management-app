from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk


class StartPage:
    def __init__(self):
        ...

    def create_root(self):
        self.root = Tk()
        self.root.configure(bg="light gray")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.title("Budget")
        self.main_menu()

    def main_menu(self):
        self.main_menu_frame = Frame(self.root)
        self.main_menu_frame.grid(row=0, column=0, sticky=NSEW)

        Label(self.main_menu_frame, text="Login to your budget manager", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=80, pady=20, ipadx=300, ipady=50)

        Label(self.main_menu_frame, text="login:", font=('Arial', 40), bg='light gray')\
            .grid(row=1, column=0)
        Entry(self.main_menu_frame)\
            .grid(row=2, column=0)
        Label(self.main_menu_frame, text="password:", font=('Arial', 40), bg='light gray')\
            .grid(row=3, column=0)
        Entry(self.main_menu_frame)\
            .grid(row=4, column=0)
        Button(self.main_menu_frame, text="Login", font=('Arial', 40), bg='light gray', command=self.login)\
            .grid(row=5, column=0)
        Label(self.main_menu_frame, text="You don't have an account?", font=('Arial', 40), bg='light gray')\
            .grid(row=6, column=0)
        Button(self.main_menu_frame, text="Create account", font=('Arial', 40), bg='light gray', command=self.create_acc)\
            .grid(row=7, column=0)
        Button(self.main_menu_frame, text="Close", font=('Arial', 40), bg='light gray', command=self.exit_from_app)\
            .grid(row=8, column=0)

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


class CreateAccount:
    def __init__(self, root):
        self.root = root

    def create_account_page(self):
        self.create_acc_page = Frame(self.root)
        self.create_acc_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.create_acc_page, text="Create your account", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=0, columnspan=3)
        Label(self.create_acc_page, text="login:", font=('Arial', 40), bg='light gray')\
            .grid(row=1, column=1)
        self.login = Entry(self.create_acc_page)\
            .grid(row=2,column=1)
        Label(self.create_acc_page, text="password:", font=('Arial', 40), bg='light gray')\
            .grid(row=3, column=1)
        self.password = Entry(self.create_acc_page)\
            .grid(row=4, column=1)
        Label(self.create_acc_page, text="repeat password:", font=('Arial', 40), bg='light gray')\
            .grid(row=5, column=1)
        self.repeat_password = Entry(self.create_acc_page)\
            .grid(row=6, column=1)
        Label(self.create_acc_page, text="e-mail", font=('Arial', 40), bg='light gray')\
            .grid(row=7, column=1)
        self.email = Entry(self.create_acc_page)\
            .grid(row=8, column=1)
        Button(self.create_acc_page, text="create account")\
            .grid(row=9, column=1)
        Button(self.create_acc_page, text="exit")\
            .grid(row=10, column=2)
        Label(self.create_acc_page, text="How should password look:\n"
                                         "-at least 8 characters\n"
                                         "-at least one big letter\n"
                                         "-at least one small letter\n"
                                         "-at least one number")\
            .grid(row=3, column=0, rowspan=7)
        Label(self.create_acc_page, text="password strength:\n"
                                         "-----------------\n"
                                         "strong")\
            .grid(row=4, column=1, rowspan=3, columnspan=2)
        Checkbutton(self.create_acc_page, text="I want to get e-mail notifications about news")\
            .grid(row=8, column=1, columnspan=2)


class LoginUser:
    def __init__(self, root):
        self.root = root

    def logged_user_page(self):
        self.logged_usr_page = Frame(self.root)
        self.logged_usr_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.logged_usr_page, text="Main page", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=0, columnspan=3)
        Button(self.logged_usr_page, text="Manage budget", font=('Arial', 40), bg='light gray')\
            .grid(row=1, column=0)
        Button(self.logged_usr_page, text="Statistics", font=('Arial', 40), bg='light gray')\
            .grid(row=2, column=0)
        Button(self.logged_usr_page, text="Shopping list", font=('Arial', 40), bg='light gray')\
            .grid(row=3, column=0)
        Button(self.logged_usr_page, text="Savings", font=('Arial', 40), bg='light gray')\
            .grid(row=1, column=1)
        Button(self.logged_usr_page, text="Receipts", font=('Arial', 40), bg='light gray')\
            .grid(row=2, column=1)
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 40), bg='light gray')\
            .grid(row=3, column=1)
        Button(self.logged_usr_page, text="Mobile app", font=('Arial', 40), bg='light gray')\
            .grid(row=4, column=0, columnspan=2)
        Button(self.logged_usr_page, text="Logout", font=('Arial', 40), bg='light gray')\
            .grid(row=4, column=2)
        Button(self.logged_usr_page, text="Logout and Exit", font=('Arial', 40), bg='light gray')\
            .grid(row=4, column=2)
        Button(self.logged_usr_page, text="Account", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=2, sticky=E)
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=2)


def main():
    run_app = StartPage()
    run_app.create_root()
    mainloop()


if __name__ == '__main__':
    main()
