import mysql.connector
import pytesseract
from PIL import Image


class ReceiptsPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        print(pytesseract.image_to_string(Image.open('test_receipt.jpg')))

    def test(self):
        ...
    # make dataframe display to user and let him edit information if there will be some mistakes in OCR conversion
