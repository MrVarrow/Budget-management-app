from tkinter import *


class QuestionnaireWindowView:
    def __init__(self, master, controller, bg_color, curr_question, question_type, question_answers):
        self.bg_color = bg_color
        self.controller = controller

        self.checklist_vars = [False, False, False, False]
        self.entry_answer = StringVar()

        # Create TopLevel window
        self.questionnaire_root = Toplevel(master, bg=bg_color)
        self.questionnaire_root.geometry("600x720")
        self.questionnaire_root.title("Download our mobile app")
        self.questionnaire_root.resizable(False, False)

        # Labels
        self.question_label = Label(self.questionnaire_root, text=curr_question, font=('Arial', 20), bg=self.bg_color,
                                    width=35, height=3, wraplength=340)
        self.question_label.grid(row=0, column=0, pady=30)

        self.create_question_frame(question_type, question_answers)

        Button(self.questionnaire_root, text="Next", font=('Arial', 15), width=10, bg="light gray",
               command=lambda: self.controller.next_question(self.entry_answer.get())) \
            .grid(row=2, column=0, sticky=E, padx=50, pady=30)

        Button(self.questionnaire_root, text="Prev", font=('Arial', 15), width=10, bg="light gray",
               command=lambda: self.controller.prev_question()) \
            .grid(row=2, column=0, sticky=W, padx=50, pady=30)

        Button(self.questionnaire_root, text="Close", font=('Arial', 15), width=7, bg="light gray",
               command=lambda: self.controller.exit()) \
            .grid(row=3, column=0, sticky=E, padx=20, pady=15)

        # Focus on TopLevel window
        self.questionnaire_root.grab_set()

    def create_question_frame(self, question_type: str, question_answers: list):
        self.question_frame = Frame(self.questionnaire_root, bg=self.bg_color, highlightbackground="black",
                                    highlightthickness=2, width=35, height=10)
        self.question_frame.grid(row=1, column=0, sticky=NSEW, padx=85, ipady=0)
        self.checklist_vars = [False, False, False, False]

        if question_type == "short_entry":
            self.question_frame.grid_configure(ipady=150)
            Label(self.question_frame, text="Type your answer here:", font=('Arial', 15), width=20) \
                .grid(row=0, column=0, sticky=W, padx=100, pady=20)
            Entry(self.question_frame, textvariable=self.entry_answer, font=('Arial', 15), width=20) \
                .grid(row=1, column=0, sticky=W, padx=100)

        elif question_type == "long_entry":
            self.question_frame.grid_configure(ipady=150)
            Label(self.question_frame, text="Type your answer here:", font=('Arial', 15), width=20) \
                .grid(row=0, column=0, sticky=W, padx=100, pady=20)
            Entry(self.question_frame, textvariable=self.entry_answer, font=('Arial', 15), width=20) \
                .grid(row=1, column=0, sticky=W, padx=100)

        elif question_type == "select_4":
            self.question_frame.grid_configure(ipady=70)
            Label(self.question_frame, text="Select one answer:", font=('Arial', 15), width=20) \
                .grid(row=0, column=0, sticky=W, padx=100, pady=20)
            for i in range(4):
                check_var = BooleanVar()
                Checkbutton(self.question_frame, text=question_answers[i], variable=check_var, font=('Arial', 12),
                            width=20, anchor="w", justify="left", height=2, wraplength=190,
                            command=lambda i=i: self.controller.check_box(i, self.checklist_vars)) \
                    .grid(row=i+1, column=0, sticky=W, padx=100)

        elif question_type == "select_2":
            self.question_frame.grid_configure(ipady=115)
            Label(self.question_frame, text="Select one answer:", font=('Arial', 15), width=20) \
                .grid(row=0, column=0, sticky=W, padx=100, pady=20)
            for i in range(2):
                check_var = BooleanVar()
                Checkbutton(self.question_frame, text=question_answers[i], variable=check_var, font=('Arial', 12),
                            width=20, anchor="w", justify="left", height=2, wraplength=190,
                            command=lambda i=i: self.controller.check_box(i, self.checklist_vars)) \
                    .grid(row=i+1, column=0, sticky=W, padx=100)

    def destroy_question_frame(self):
        self.entry_answer.set("")
        self.question_frame.destroy()

    def update_question(self, new_question: str):
        self.question_label.configure(text=new_question)

    def close_window(self):
        self.questionnaire_root.destroy()
