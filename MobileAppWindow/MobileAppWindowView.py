from tkinter import *


class MobileAppWindowView:
    def __init__(self, master, controller, bg_color, curr_question, question_type, question_answers):
        self.bg_color = bg_color
        self.controller = controller

        self.checklist_vars = [False, False, False, False]
        self.entry_answer = StringVar()


        # Create TopLevel window
        self.mobile_app_root = Toplevel(master, bg=bg_color)
        self.mobile_app_root.geometry("600x720")
        self.mobile_app_root.title("Download our mobile app")
        self.mobile_app_root.resizable(False, False)

        # Labels
        self.question_label = Label(self.mobile_app_root, text=curr_question, font=('Arial', 15), bg=self.bg_color, width=50, height=3)
        self.question_label.grid(row=0, column=0, pady=10)

        self.create_question_frame(question_type, question_answers)

        Button(self.mobile_app_root, text="Next", font=('Arial', 15), width=6, command=lambda: self.controller.next_question(self.entry_answer.get())) \
            .grid(row=2, column=0, sticky=E)

        Button(self.mobile_app_root, text="Prev", font=('Arial', 15), width=6) \
            .grid(row=2, column=0, sticky=W)

        Button(self.mobile_app_root, text="Close", font=('Arial', 15), width=7, command=lambda: self.controller.exit()) \
            .grid(row=3, column=0, sticky=W)

        # Focus on TopLevel window
        self.mobile_app_root.grab_set()


    def create_question_frame(self, question_type, question_answers):
        self.question_frame = Frame(self.mobile_app_root, bg=self.bg_color)
        self.question_frame.grid(row=1, column=0, sticky=NSEW)
        self.checklist_vars = [False, False, False, False]
        if question_type == "short_entry":

            Entry(self.question_frame, textvariable=self.entry_answer).grid()
        elif question_type == "long_entry":

            Entry(self.question_frame, textvariable=self.entry_answer).grid()
        elif question_type == "select_4":
            for i in range(4):
                check_var = BooleanVar()
                Checkbutton(self.question_frame, text=question_answers[i], variable=check_var, command=lambda i=i: self.controller.check_box(i, self.checklist_vars)).grid()
        elif question_type == "select_2":
            for i in range(2):
                check_var = BooleanVar()
                Checkbutton(self.question_frame, text=question_answers[i], variable=check_var, command=lambda i=i: self.controller.check_box(i, self.checklist_vars)).grid()

    def destroy_question_frame(self):
        self.entry_answer.set("")
        self.question_frame.destroy()

    def update_question(self, new_question):
        self.question_label.configure(text=new_question)

    def close_window(self):
        self.mobile_app_root.destroy()
