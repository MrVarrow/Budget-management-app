from tkinter import *


class SettingsPageView:
    def __init__(self, master, controller, bg_color):
        self.controller = controller
        self.master = master
        self.bg_color_state = BooleanVar()
        self.bg_color = bg_color
        # Icon loading and scaling
        self.send_message_icon = PhotoImage(file="Icons/message.png")
        self.send_message_icon = self.send_message_icon.subsample(20, 20)

        # Frame creation
        self.settings_page = Frame(master, bg=self.bg_color)
        self.settings_page.grid(row=0, column=0, sticky=NSEW)

        # Labels
        Label(self.settings_page, text="Settings", font=('Arial', 40), bg="light gray") \
            .grid(row=0, column=0, sticky=EW, padx=330, pady=30, ipadx=220, ipady=50)

        # Dark mode checkbutton
        self.dark_mode = Checkbutton(self.settings_page, text="Dark mode", font=('Arial', 20), bg="light gray", borderwidth=2,
                    relief="solid", command=lambda: controller.dark_mode(), variable=self.bg_color_state,
                    onvalue=True, offvalue=False)
        self.dark_mode.grid(row=3, column=0, pady=40)

        # Support and help button
        Button(self.settings_page, text="Support and Help", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.support_and_help()) \
            .grid(row=1, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # App version button
        Button(self.settings_page, text="App version", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.app_version()) \
            .grid(row=1, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Credits button
        Button(self.settings_page, text="Credits", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.credits()) \
            .grid(row=2, column=0, sticky=W, padx=200, pady=40, ipady=5)

        # About app button
        Button(self.settings_page, text="About app", font=('Arial', 20), width=15, bg="light gray",
               command=lambda: controller.about_app()) \
            .grid(row=2, column=0, sticky=E, padx=200, pady=40, ipady=5)

        # Close button
        Button(self.settings_page, text="Close", font=('Arial', 15), bg="light gray", width=8,
               command=lambda: controller.back()) \
            .grid(row=4, column=0, sticky=SE, padx=30, pady=10, ipady=5)

        self.select_checkbutton_if_dark()

    # If dark mode is on auto select checkbutton
    def select_checkbutton_if_dark(self):
        if self.bg_color == "gray":
            self.dark_mode.select()

    # Destroying frame
    def destroy_setting_page_frame(self):
        self.settings_page.destroy()

    # Credits window creation
    def credits_window_create(self):
        # Window creation
        self.credits_root = Toplevel(self.master, bg=self.bg_color)
        self.credits_root.geometry("400x200")
        self.credits_root.title("Credits")
        self.credits_root.resizable(False, False)

        # Labels
        Label(self.credits_root, text="Credits", font=('Arial', 15))\
            .grid(row=0, column=0, padx=150, pady=10)
        Label(self.credits_root, text="This App is fully created by Franciszek Gawadziński\n"
                                      "(Varrow)", font=('Arial', 12))\
            .grid(row=1, column=0)
        Label(self.credits_root, text="Visit me on Github and Linkedin!", font=('Arial', 12))\
            .grid(row=2, column=0)

        # Github link button
        github_button = Button(self.credits_root, text="https://github.com/MrVarrow", font=('Arial', 9), fg='blue',
                               bd=0, command=lambda: self.controller.credits_github(github_button.cget("text")))
        github_button.grid(row=3, column=0)

        # Linkedin link button
        linkedin_button = Button(self.credits_root, text="https://www.linkedin.com/in/franciszek-gawadzi%C5%84ski-5493492b0",
                                 font=('Arial', 9), fg='blue', bd=0,
                                 command=lambda: self.controller.credits_linkedin(linkedin_button.cget("text")))
        linkedin_button.grid(row=4, column=0)

        # Close button
        Button(self.credits_root, text="Close", font=('Arial', 15), bg="light gray",
               command=lambda: self.destroy_credits_window())\
            .grid(row=5, column=0, sticky=E)

        # Focus on credits window
        self.credits_root.grab_set()

    # Change color to dark or light based on current background
    def bg_color_change(self):
        if self.bg_color == "#f0f0f0":
            self.bg_color = "gray"
            self.settings_page.configure(bg=self.bg_color)
            return self.bg_color

        elif self.bg_color == "gray":
            self.bg_color = "#f0f0f0"
            self.settings_page.configure(bg=self.bg_color)
            return self.bg_color

    # Destroying credits window
    def destroy_credits_window(self):
        self.credits_root.destroy()

    # Creates support and help window
    def support_and_help_window(self):
        self.chatbot_root = Toplevel(self.master, bg=self.bg_color)
        self.chatbot_root.geometry("400x200")
        self.chatbot_root.title("Credits")
        self.chatbot_root.resizable(False, False)
        question = StringVar()

        # Frames
        self.answer_frame = Frame(self.chatbot_root, bg=self.bg_color)
        self.answer_frame.grid(row=1, column=0)

        # Labels
        Label(self.chatbot_root, text="Welcome to chatbot. I'm here to help you!\n"
                                      "Type your question below.", font=('Arial', 12)) \
            .grid(row=0, column=0, padx=55, pady=5)

        Label(self.answer_frame, text="", borderwidth=2, relief="solid", width=40, height=5, font=('Arial', 12)) \
            .grid(row=0, column=0, pady=5)

        self.entry_question = Entry(self.chatbot_root, font=('Arial', 12), width=35, textvariable=question)
        self.entry_question.grid(row=3, column=0, pady=5, sticky=W, padx=10)

        # Enter question button
        Button(self.chatbot_root, image=self.send_message_icon,
               command=lambda: self.controller.update_answer(question.get()),
               bg="light gray") \
            .grid(row=3, column=0, sticky=E, padx=10)

    # Updates label widget to show answer
    def update_answer_widget(self, answer):
        self.answer_frame.destroy()

        self.answer_frame = Frame(self.chatbot_root, bg=self.bg_color)
        self.answer_frame.grid(row=1, column=0)

        Label(self.answer_frame, text=answer, borderwidth=2, relief="solid", width=40, height=5,
              font=('Arial', 12), wraplength=350) \
            .grid(row=0, column=0, pady=5)

        self.clear_entry_widget()

    # Clearing entry widget
    def clear_entry_widget(self):
        self.entry_question.delete(0, END)
