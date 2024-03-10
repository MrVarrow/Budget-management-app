from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk


#to do wyjścia, ikonki, show password,

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
        self.photo = PhotoImage(file="hide.png")
        self.photo = self.photo.subsample(20, 20)
        print(type(self.photo))

        self.main_menu_frame = Frame(self.root)
        self.main_menu_frame.grid(row=0, column=0, sticky=NSEW)

        Label(self.main_menu_frame, text="Login to your budget manager", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=80, pady=20, ipadx=220, ipady=50)

        Label(self.main_menu_frame, text="login:", font=('Arial', 20))\
            .grid(row=1, column=0, padx=500, sticky=W)
        Entry(self.main_menu_frame, font=('Arial', 20))\
            .grid(row=2, column=0, padx=500, sticky=W, pady=10)
        Label(self.main_menu_frame, text="password:", font=('Arial', 20))\
            .grid(row=3, column=0, padx=500, sticky=W)
        Entry(self.main_menu_frame, font=('Arial', 20))\
            .grid(row=4, column=0, padx=500, sticky=W, pady=10)
        #show password need icon
        Button(self.main_menu_frame, text="S", bg='light gray', image=self.photo)\
            .grid(row=4, column=0, padx=470, sticky=E)
        Button(self.main_menu_frame, text="Login", font=('Arial', 25), bg='light gray', command=self.login)\
            .grid(row=5, column=0, padx=580, sticky=W, pady=50, ipadx=20)
        Label(self.main_menu_frame, text="You don't have an account?", font=('Arial', 15))\
            .grid(row=6, column=0, padx=530, sticky=W, pady=5)
        Button(self.main_menu_frame, text="Create account", font=('Arial', 15), bg='light gray', command=self.create_acc)\
            .grid(row=7, column=0)
        Button(self.main_menu_frame, text="Close", font=('Arial', 20), bg='light gray', command=self.exit_from_app)\
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
        ...


class CreateAccount:
    def __init__(self, root):
        self.root = root

    def create_account_page(self):
        self.create_acc_page = Frame(self.root)
        self.create_acc_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.create_acc_page, text="Create your account", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=0, columnspan=3, sticky=EW, padx=100, pady=10, ipadx=310, ipady=50)
        Label(self.create_acc_page, text="login:", font=('Arial', 20))\
            .grid(row=1, column=1, padx=450, sticky=W)
        self.login = Entry(self.create_acc_page, font=('Arial', 20))\
            .grid(row=2,column=1, padx=450, sticky=W, pady=10)
        Label(self.create_acc_page, text="password:", font=('Arial', 20))\
            .grid(row=3, column=1, padx=450, sticky=W)
        self.password = Entry(self.create_acc_page, font=('Arial', 20))\
            .grid(row=4, column=1, padx=450, sticky=W, pady=10)
        Label(self.create_acc_page, text="repeat password:", font=('Arial', 20))\
            .grid(row=5, column=1, padx=450, sticky=W)
        self.repeat_password = Entry(self.create_acc_page, font=('Arial', 20))\
            .grid(row=6, column=1, padx=450, sticky=W, pady=10)
        Label(self.create_acc_page, text="e-mail:", font=('Arial', 20))\
            .grid(row=7, column=1, padx=450, sticky=W)
        self.email = Entry(self.create_acc_page, font=('Arial', 20))\
            .grid(row=8, column=1, padx=450, sticky=W, pady=10)
        Button(self.create_acc_page, text="create account", font=('Arial', 25), bg="light gray")\
            .grid(row=9, column=1, pady=10)
        Button(self.create_acc_page, text="exit", font=('Arial', 20), bg="light gray")\
            .grid(row=10, column=1, pady=10, ipadx=20, sticky=E, padx=5)
        Label(self.create_acc_page,  font=('Arial', 12), borderwidth=2, relief="solid", text="How should password look:\n"
                                         "-at least 8 characters\n"
                                         "-at least one big letter\n"
                                         "-at least one small letter\n"
                                         "-at least one number")\
            .grid(row=3, column=1, rowspan=7, sticky=NW, padx=150, pady=45, ipadx=20, ipady=20)
        Label(self.create_acc_page, font=('Arial', 12), borderwidth=2, relief="solid", text="password strength:\n"
                                         "-----------------\n"
                                         "strong")\
            .grid(row=4, column=1, rowspan=3, columnspan=2, sticky=SE, padx=300, pady=25, ipadx=20, ipady=20)
        Checkbutton(self.create_acc_page, text="I want to get e-mail notifications about news", font=('Arial', 12))\
            .grid(row=8, column=1, columnspan=2, sticky=E, padx=150)

    def create_acc(self):
        ...

    def exit_from_create_acc(self):
        ...

class LoginUser:
    def __init__(self, root):
        self.root = root


    def logged_user_page(self):
        self.acc_icon = PhotoImage(file="user.png")
        self.acc_icon = self.acc_icon.subsample(20, 20)
        self.photo = PhotoImage(file="gear.png")
        self.photo = self.photo.subsample(20, 20)



        self.logged_usr_page = Frame(self.root)
        self.logged_usr_page.grid(row=0, column=0, sticky=NSEW)

        Label(self.logged_usr_page, text="Main page", font=('Arial', 40), bg='light gray')\
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=225, pady=40, ipadx=210, ipady=50)
        Button(self.logged_usr_page, text="Manage budget", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=1, column=0, pady=20)
        Button(self.logged_usr_page, text="Statistics", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=2, column=0, pady=20)
        Button(self.logged_usr_page, text="Shopping list", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=3, column=0, pady=20)
        Button(self.logged_usr_page, text="Savings", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=1, column=1, pady=20)
        Button(self.logged_usr_page, text="Receipts", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=2, column=1, pady=20)
        Button(self.logged_usr_page, text="Rate us!", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=3, column=1, pady=20)
        Button(self.logged_usr_page, text="Mobile app", font=('Arial', 20), bg='light gray', width=15)\
            .grid(row=4, column=0, columnspan=2, pady=65)
        Button(self.logged_usr_page, text="Logout", font=('Arial', 20), bg='light gray')\
            .grid(row=4, column=2, sticky=NE, padx=20, pady=50, ipadx=10)
        Button(self.logged_usr_page, text="Exit", font=('Arial', 20), bg='light gray')\
            .grid(row=4, column=2, sticky=SE, padx=20, pady=10, ipadx=30)
        #your acc need icon
        xxx = Button(self.logged_usr_page, text="A", bg='light gray', image=self.acc_icon)
        xxx.image = self.acc_icon
        xxx.grid(row=0, column=2, sticky=NE, padx=20, pady=10)
        #settings need icon
        # fix other icons like above
        Button(self.logged_usr_page, text="S", bg='light gray', image=self.photo)\
            .grid(row=0, column=2, sticky=NW, padx=30, pady=10)

    def settings(self):
        ...

    def your_acc(self):
        ...

    def logout(self):
        ...

    def exit(self):
        ...

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
