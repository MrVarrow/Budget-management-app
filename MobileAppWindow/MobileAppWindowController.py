from MobileAppWindow.MobileAppWindowModel import MobileAppWindowsModel
from MobileAppWindow.MobileAppWindowView import MobileAppWindowView


class MobileAppWindowController:
    def __init__(self, root, user_data, bg_color):
        self.root = root
        self.bg_color = bg_color
        self.user_data = user_data
        self.curr_question_index = 0
        self.mobile_app_window_model = MobileAppWindowsModel()
        self.questions_dict = self.mobile_app_window_model.get_questions_with_answers()
        self.questions_list = list(self.questions_dict.keys())
        self.mobile_app_window_view = MobileAppWindowView(self.root, self, self.bg_color, self.curr_question_index, self.curr_question, self.curr_question_type, self.curr_question_answers)

    # Copy link when user press the button
    def copy_link(self, link):
        self.mobile_app_window_model.copy_app_link(link)

    # Sending email when user press the button
    def send_email_with_link(self, link):
        self.mobile_app_window_model.send_email_with_link(link, self.user_data[1])

    def next_question(self):
        ...
        if self.curr_question_index < len(self.questions_list):
            self.curr_question_index += 1

    def prev_question(self):
        ...
        if self.curr_question_index > 0:
            self.curr_question_index -= 1

    def exit(self):
        ...
