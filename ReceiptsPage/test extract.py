import easyocr
import pandas as pd
import cv2
import pandas
import numpy as np
from matplotlib import pyplot as plt

def draw_bounding_boxes(image, detections, threshold=0.25):

    for bbox, text, score in detections:

        if score > threshold:

            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)

            cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)


img = cv2.imread("test_receipt_v2.jpg")
reader = easyocr.Reader(['pl'], gpu=False)
text_detections = reader.readtext(img)

threshold = 0.25

data = []
for result in text_detections:
    text = result[1]  # Text is the second element in the tuple
    bbox = result[0]  # Bounding box coordinates are the first element
    x1, y1, x2, y2 = bbox  # Unpack the bounding box coordinates
    data.append({'text': text})

df = pd.DataFrame(data)
print(df)
draw_bounding_boxes(img, text_detections, threshold)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))

plt.show()






