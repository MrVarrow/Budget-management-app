from MobileAppWindow.MobileAppWindowModel import MobileAppWindowsModel
from MobileAppWindow.MobileAppWindowView import MobileAppWindowView
from tkinter import messagebox


class MobileAppWindowController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data

        self.curr_question_index = 0
        self.checkbutton_list = []
        self.answer_list = []

        self.mobile_app_window_model = MobileAppWindowsModel()
        self.questions_dict = self.mobile_app_window_model.get_questions_with_answers()
        self.questions_list = list(self.questions_dict.keys())
        self.curr_question_type, self.curr_question_answers = self.mobile_app_window_model.get_type_and_answers(self.questions_list[self.curr_question_index])

        self.mobile_app_window_view = MobileAppWindowView(self.root, self, self.bg_color, self.questions_list[self.curr_question_index], self.curr_question_type, self.curr_question_answers)

    def next_question(self, answer):
        ans = self.mobile_app_window_model.look_for_true(self.checkbutton_list)
        self.checkbutton_list = []

        if not answer == "":
            self.answer_list.append(answer)  # ENTRY
            print(self.curr_question_index, len(self.questions_list))
            if self.curr_question_index < len(self.questions_list) - 1:
                self.curr_question_index += 1
                self.switch_view()
                return
            else:
                user_info_dict = self.mobile_app_window_model.update_dict(self.answer_list)
                print(user_info_dict)
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
            user_info_dict = self.mobile_app_window_model.update_dict(self.answer_list)
            return

    def switch_view(self):
        self.mobile_app_window_view.destroy_question_frame()
        self.mobile_app_window_view.update_question(self.questions_list[self.curr_question_index])
        self.curr_question_type, self.curr_question_answers = self.mobile_app_window_model.get_type_and_answers(
            self.questions_list[self.curr_question_index])
        self.mobile_app_window_view.create_question_frame(self.curr_question_type, self.curr_question_answers)

    def prev_question(self):
        ...
        if self.curr_question_index > 0:
            self.curr_question_index -= 1

    def exit(self):
        self.mobile_app_window_view.close_window()

    # Tracks state of every checkbox state and update its value in list
    def check_box(self, index: int, check_vars: list):
        self.checkbutton_list = self.mobile_app_window_model.toggle_checkbutton(index, check_vars)
