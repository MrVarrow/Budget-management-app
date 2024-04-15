import mysql.connector


class ReceiptsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def test(self):
        ...
    # make dataframe display to user and let him edit information if there will be some mistakes in OCR
