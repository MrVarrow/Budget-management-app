import os
import mysql.connector
import webbrowser
import json
from difflib import get_close_matches
from typing import Union


class SettingsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Opens my github profile when link is pressed
    @staticmethod
    def credits_github_link(url: str):
        webbrowser.open_new(url)

    # Opens my linkedin profile when link is pressed
    @staticmethod
    def credits_linkedin_link(url: str):
        webbrowser.open_new(url)

    # Open json file, load  and return data from it
    @staticmethod
    def load_knowledge_base(file_path: str) -> dict:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

    # Get the best matching answer for question and return result
    @staticmethod
    def find_answer(user_question: str, questions: list) -> Union[str, None]:
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    # Get the answer that is assigned to a question that was chosen by find_answer
    @staticmethod
    def get_answer_for_question(question: str, chatbot_db: dict) -> str:
        for q in chatbot_db["questions"]:
            if q["question"] == question:
                return q["answer"]

    # This method runs an assistant and returning answer
    def chat_bot(self, user_input: str) -> str:
        chatbot_db = self.load_knowledge_base(r"SettingsPage\ChatbotDB.json")

        while True:
            best_answer = self.find_answer(user_input, [q["question"] for q in chatbot_db["questions"]])

            if best_answer:
                answer = self.get_answer_for_question(best_answer, chatbot_db)
                return answer
            else:
                message = "any of the answers match your question, if you need help please contact support via email"
                return message

    # Opens about app txt file
    @staticmethod
    def open_about_app_file():
        os.startfile("AboutApp.txt")
