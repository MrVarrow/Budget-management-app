import mysql.connector
import webbrowser


class SettingsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Opens my github profile when link is pressed
    def credits_github_link(self, url):
        webbrowser.open_new(url)

    # Opens my linkedin profile when link is pressed
    def credits_linkedin_link(self, url):
        webbrowser.open_new(url)
