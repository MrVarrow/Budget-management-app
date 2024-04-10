import pytesseract
import cv2
import easyocr
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
# to fix
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image):
    # Load the image


    # Scale the image
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's binarization
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Apply Gaussian blurring to remove noise
    blurred = cv2.GaussianBlur(binary, (5, 5), 0)

    #Enhance contrast
    enhanced = cv2.equalizeHist(blurred)

    return enhanced


def read_text(image1):
    image = preprocess_image(image1)
    reader = easyocr.Reader(['en'], gpu=False)
    text_detections = reader.readtext(image)
    data = ""
    for result in text_detections:
        text = result[1]
        bbox = result[0]  # Bounding box coordinates are the first element
        x1, y1, x2, y2 = bbox
        data += text
    # draw_bounding_boxes(img, text_detections, threshold)
    cv2.imwrite('1083-receipt_roi_fixed.png', image)

    return data

image = cv2.imread("1083-receipt.png")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("1083-receipt_gray.png", gray)

blur = cv2.GaussianBlur(gray,(7,7), 0)
cv2.imwrite('1083-receipt_blur.png', blur)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite('1083-receipt_thresh.png', thresh)

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (22, 5))
cv2.imwrite('1083-receipt_kernal.png', kernal)

dilate = cv2.dilate(thresh, kernal, iterations=1)
cv2.imwrite('1083-receipt_dilate.png', dilate)


cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

results = []
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)

    if h < 100 and w < 300:
        #cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
        roi = image[y:y + h, x:x + w]
        cv2.imwrite('1083-receipt_roi.png', roi)
        ocr_result = read_text(roi)
        results.append(ocr_result)
            # Crop the image to the bounding box
        #ocr_result = pytesseract.image_to_string(roi)

        #ocr_result = ocr_result.split("\n")
        #for item in ocr_result:
            #results.append(item)

print(results)
#cv2.imwrite('1083-receipt_bbox.png', image)

