from tkinter import *


class UserLoginView:
    def __init__(self, master, controller, bg_color):
        # Loading icon and scaling it
        self.show_password_icon = PhotoImage(file="Icons/hide.png")
        self.show_password_icon = self.show_password_icon.subsample(20, 20)
        self.bg_color = bg_color

        # Define variables for entries
        self.password = StringVar()
        self.login = StringVar()

        # Frame create
        self.main_menu_frame = Frame(master, bg=self.bg_color)
        self.main_menu_frame.grid(row=0, column=0, sticky=NSEW)

        # Labels and Entries
        Label(self.main_menu_frame, text="Login to your budget manager", font=('Arial', 40), bg='light gray') \
            .grid(row=0, column=0, columnspan=2, sticky=EW, padx=80, pady=20, ipadx=220, ipady=50)

        Label(self.main_menu_frame, text="You don't have an account?", font=('Arial', 15)) \
            .grid(row=7, column=0, padx=530, sticky=W, pady=5)

        Label(self.main_menu_frame, text="login:", font=('Arial', 20)) \
            .grid(row=1, column=0, padx=500, sticky=W)
        Entry(self.main_menu_frame, font=('Arial', 20), textvariable=self.login) \
            .grid(row=2, column=0, padx=500, sticky=W, pady=10)

        Label(self.main_menu_frame, text="password:", font=('Arial', 20)) \
            .grid(row=3, column=0, padx=500, sticky=W)
        self.password_entry = Entry(self.main_menu_frame, font=('Arial', 20), show="*", textvariable=self.password)
        self.password_entry.grid(row=4, column=0, padx=500, sticky=W, pady=10)

        # Show Password button
        self.show_password_icon_widget = Button(self.main_menu_frame, text="S", bg='light gray',
                                                image=self.show_password_icon, command=self.show_password)
        self.show_password_icon_widget.image = self.show_password_icon
        self.show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)

        # Forgot Password button
        Button(self.main_menu_frame, text="Forgot your password?", fg='blue', font=('Arial', 10, 'underline'), bd=0,
               command=lambda: controller.forgot_pass(self.login.get())) \
            .grid(row=5, column=0)

        # Login button
        Button(self.main_menu_frame, text="Login", font=('Arial', 25), bg='light gray',
               command=lambda: controller.user_login(self.login.get(), self.password.get())) \
            .grid(row=6, column=0, padx=580, sticky=W, pady=35, ipadx=20)

        # Create account button
        Button(self.main_menu_frame, text="Create account", font=('Arial', 15), bg='light gray',
               command=controller.create_acc) \
            .grid(row=8, column=0)
        # Close button
        Button(self.main_menu_frame, text="Close", font=('Arial', 20), bg='light gray',
               command=controller.exit_from_app) \
            .grid(row=9, column=0, sticky=SE, padx=40, ipadx=20, pady=20)

    # Showing password and changing usage of button to hide password
    def show_password(self):
        self.show_password_icon_widget.destroy()
        self.show_password_icon_widget = Button(self.main_menu_frame, bg='light gray',
                                                image=self.show_password_icon, command=self.hide_password)
        self.show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)
        self.password_entry.config(show="")

    # Hiding password and changing usage of button to show password
    def hide_password(self):
        self.show_password_icon_widget.destroy()
        self.show_password_icon_widget = Button(self.main_menu_frame, bg='light gray',
                                                image=self.show_password_icon, command=self.show_password)
        self.show_password_icon_widget.grid(row=4, column=0, padx=470, sticky=E)
        self.password_entry.config(show="*")

    # Destroying frame
    def destroy_login_page_frame(self):
        self.main_menu_frame.destroy()
