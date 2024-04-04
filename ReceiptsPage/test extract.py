
import pytesseract
from PIL import Image, ImageEnhance
import cv2
import pandas
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread("test.png")

img3 = cv2.imread("test_receipt_v2.jpg")
#img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
#img3 = Image.open("test_receipt_v2.jpg")
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)





#cv2.imwrite("stripped.png", img3)


data = pytesseract.image_to_string(img3, output_type='string')

print(data)

