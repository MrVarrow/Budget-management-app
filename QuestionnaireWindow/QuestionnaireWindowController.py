from QuestionnaireWindow.QuestionnaireWindowModel import QuestionnaireWindowsModel
from QuestionnaireWindow.QuestionnaireWindowView import QuestionnaireWindowView
from tkinter import messagebox


class QuestionnaireWindowController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.curr_question_index = 0
        self.checkbutton_list = []
        self.answer_list = []

        self.questionnaire_window_model = QuestionnaireWindowsModel()
        self.questions_dict = self.questionnaire_window_model.get_questions_with_answers()
        self.questions_list = list(self.questions_dict.keys())
        self.curr_question_type, self.curr_question_answers = self.questionnaire_window_model.get_type_and_answers(
            self.questions_list[self.curr_question_index])

        self.questionnaire_window_view = QuestionnaireWindowView(self.root, self, self.bg_color,
                                                                 self.questions_list[self.curr_question_index],
                                                                 self.curr_question_type, self.curr_question_answers)

    def next_question(self, answer: str):
        ans = self.questionnaire_window_model.look_for_true(self.checkbutton_list)
        self.checkbutton_list = []

        if not answer == "":
            self.answer_list.append(answer)  # ENTRY
            if self.curr_question_index < len(self.questions_list) - 1:
                self.curr_question_index += 1
                self.switch_view()
                return
            else:
                if self.questionnaire_window_model.get_questionnaire_info(self.user_data):
                    self.questionnaire_window_model.update_data_in_database(self.user_data, self.answer_list)
                    messagebox.showinfo(title="Information", message="Answers successfully updated. Thank You!")

                    self.questionnaire_window_view.close_window()
                else:
                    self.questionnaire_window_model.insert_data_to_database(self.user_data, self.answer_list)
                    messagebox.showinfo(title="Information", message="Answers successfully send. Thank You!")

                    self.questionnaire_window_view.close_window()
                return

        if not ans == "Error":
            self.answer_list.append(self.curr_question_answers[ans])
        elif ans == "Error":
            messagebox.showinfo(title="Information", message="Please select one answer.")
            return

        if self.curr_question_index < len(self.questions_list) - 1:
            self.curr_question_index += 1
            self.switch_view()
            return
        else:
            ...
            # would only happen if last question is type: select, currently isn't
            return

    # switching view to next or prev question
    def switch_view(self):
        self.questionnaire_window_view.destroy_question_frame()
        self.questionnaire_window_view.update_question(self.questions_list[self.curr_question_index])
        self.curr_question_type, self.curr_question_answers = self.questionnaire_window_model.get_type_and_answers(
            self.questions_list[self.curr_question_index])
        self.questionnaire_window_view.create_question_frame(self.curr_question_type, self.curr_question_answers)

    def prev_question(self):
        if self.curr_question_index == 0:
            messagebox.showinfo(title="Information", message="That's first question.")
            return
        else:
            self.curr_question_index -= 1
            self.answer_list.pop()
            self.switch_view()
            return

    def exit(self):
        self.questionnaire_window_view.close_window()

    # Tracks state of every checkbox state and update its value in list
    def check_box(self, index: int, check_vars: list):
        self.checkbutton_list = self.questionnaire_window_model.toggle_checkbutton(index, check_vars)
