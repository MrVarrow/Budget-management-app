import cv2
import pytesseract
import os
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Resize image for better OCR performance
    height, width = image.shape[:2]
    new_width = 800  # Set a standard width
    new_height = int((new_width / width) * height)
    resized_image = cv2.resize(image, (new_width, new_height))

    # Convert to grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Deskewing (if necessary)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = gray.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    gray = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Denoise the image
    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

    # Apply Otsu's thresholding
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological operations to clean up the image
    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return morph


def adjust_brightness_contrast(image):
    # Convert to float32 for better precision
    img_float = np.float32(image)

    # Adjust brightness and contrast
    img_float = cv2.convertScaleAbs(img_float, alpha=1.5, beta=30)  # Adjust alpha and beta as needed

    return img_float


# Example usage
image_path = '1000-receipt.png'
processed_image = preprocess_image(image_path)

# Save processed image for debugging
cv2.imwrite('processed_receipt.png', processed_image)


def find_receipt_contour(edged_image):
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours by area and get the largest one
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Assume the largest contour is the receipt
    return contours[0] if contours else None


# Example usage
receipt_contour = find_receipt_contour(processed_image)


def warp_receipt(image, contour):
    # Get bounding box coordinates
    rect = cv2.boundingRect(contour)
    x, y, w, h = rect

    # Crop and warp the image to get a top-down view of the receipt
    warped = image[y:y + h, x:x + w]

    return warped


# Example usage
original_image = cv2.imread(image_path)
warped_receipt = warp_receipt(original_image, receipt_contour)

# Save warped image for debugging
cv2.imwrite('warped_receipt.png', warped_receipt)


def extract_text_from_receipt(warped_image):
    custom_config = r'--oem 3 --psm 4'  # Test different PSM values
    text = pytesseract.image_to_string(warped_image, config=custom_config)

    return text


# Example usage
extracted_text = extract_text_from_receipt(warped_receipt)
print("Extracted Text:\n", extracted_text)


def extract_product_price_pairs(text):
    items = []

    # Regular expression pattern for item descriptions and prices
    # This pattern captures lines where there is a product name followed by a price
    item_pattern = r'(\d+\s+[A-Za-z\s\.\$]+)\s+([\d.,]+)'  # Match item name and price

    # Split the text into lines and process each line
    for line in text.split('\n'):
        line = line.strip()
        print(f"Processing line: '{line}'")  # Debugging output

        match = re.search(item_pattern, line)
        if match:
            item_name = match.group(1).strip()
            price = match.group(2).replace(',', '.').strip()
            items.append((item_name, price))

    return items


def clean_extracted_text(text):


    return text


# Example usage
cleaned_text = clean_extracted_text(extracted_text)
parsed_items = extract_product_price_pairs(cleaned_text)

print("Parsed Items:\n", parsed_items)