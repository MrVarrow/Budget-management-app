from tkinter import *


class MobileAppWindowView:
    def __init__(self, master, controller, bg_color, curr_question, questions_list):
        self.bg_color = bg_color
        # Loading icons and scaling them
        copy_icon = PhotoImage(file="Icons/copy.png")
        copy_icon = copy_icon.subsample(20, 20)
        email_icon = PhotoImage(file="Icons/email.png")
        email_icon = email_icon.subsample(20, 20)

        # Create TopLevel window
        self.mobile_app_root = Toplevel(master, bg=bg_color)
        self.mobile_app_root.geometry("600x720")
        self.mobile_app_root.title("Download our mobile app")
        self.mobile_app_root.resizable(False, False)

        # Labels
        Label(self.mobile_app_root, text=questions_list[curr_question], font=('Arial', 15), bg=self.bg_color) \
            .grid(row=0, column=0, pady=10)

        # Focus on TopLevel window
        self.mobile_app_root.grab_set()


    def create_question_frame(self, curr_question, question_type, question_answers):
        self.question_frame = Frame(self.mobile_app_root, bg=self.bg_color)
        self.question_frame.grid(row=0, column=0, sticky=NSEW)

        Label(self.question_frame, text=curr_question).grid()

        if question_type == "short_entry":
            ...
        elif question_type == "long_entry":
            ...
        elif question_type == "select_4":
            ...
        elif question_type == "select_2":
            ...
    def destroy_question_frame(self):
        ...
