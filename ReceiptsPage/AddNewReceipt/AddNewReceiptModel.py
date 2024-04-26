import mysql.connector
import pandas as pd
from tkinter import filedialog
import re
from datetime import date
import cv2
from joblib import load


class AddNewReceiptModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    '''
    ADD METHODS
    '''

    # Creating base of dataframe
    def create_df(self):
        items_df = pd.DataFrame(columns=["Item name", "Item price"])
        return items_df

    # Adding items to dataframe
    def add_items_to_df(self, item_name, item_price, items_df):
        new_row = {"Item name": item_name, "Item price": item_price}
        new_df = pd.DataFrame([new_row], index=[len(items_df)])
        updated_df = pd.concat([items_df, new_df], ignore_index=False)
        return updated_df

    # Delete selected item from dataframe
    def delete_from_df(self, item_name, items_df):
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        return items_df

    # Choose file to photo via filedialog
    def choose_file(self):
        filepath = filedialog.askopenfilename()
        return filepath

    # Counts number of items in receipt
    def item_count_in_receipt(self, items_df):
        num_rows = len(items_df.index)
        return num_rows

    # Calculates total price of receipt
    def calculate_total_price(self, items_df):
        prices = items_df['Item price'].tolist()
        total = 0
        for price in prices:
            total += float(price)
        return total

    # Adding receipt to database
    def add_receipt_to_database(self, user_data, receipt_name, item_count, creation_date):
        insert_query = 'INSERT INTO `receipts` (UserName, ReceiptName, ItemsCount, CreationDate)' \
                       ' VALUES (%s, %s, %s, %s)'
        values_to_insert = (user_data[0], receipt_name, str(item_count), creation_date)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Gets receipt id from database
    def get_receipt_id(self, receipt_name):
        self.cursor.execute('SELECT ReceiptID FROM `receipts` WHERE ReceiptName = %s', (receipt_name,))
        row = self.cursor.fetchone()
        receipt_id = row[0]
        return receipt_id

    # Adding items from receipt to database and assign it to receipt id
    def add_items_to_database(self, receipt_id, user_data, items_df, total):
        for index, row in items_df.iterrows():
            item, price = self.get_items_and_prices(row)
            insert_query = 'INSERT INTO `receiptitems` (ReceiptID, Username, Item, Price, TotalPrice)' \
                           ' VALUES (%s, %s, %s, %s, %s)'
            values_to_insert = (receipt_id, user_data[0], item, price, total)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    # Get time of receipt creation in system
    def get_creation_time(self):
        creation_date = date.today()
        return creation_date

    # Gets item name and its price
    def get_items_and_prices(self, row):
        name = row["Item name"]
        price = row["Item price"]

        return name, price

    # Check if product name is correct
    def check_product_name(self, item_name):
        if re.search(r"\W", item_name) or re.search("[0-9]", item_name):
            return False
        return True

    # Check if product price is correct
    def check_product_price(self, item_price):
        if not re.search(r'^\d+(?:[.]\d{1,2}|$)$', item_price):
            return False
        return True

    # Check if receipt name is correct
    def check_receipt_name(self, receipt_name):
        if re.search(r"\W", receipt_name):
            return False
        return True

    # Check if receipt name is unique
    def check_for_duplicates(self):
        ...

    '''
    UPDATE METHODS
    '''

    # Updates item count
    def update_item_count(self, item_count, receipt_id):
        self.cursor.execute('UPDATE `receipts` SET ItemsCount = %s WHERE ReceiptID = %s', (item_count, receipt_id))
        self.connection.commit()

    # Delete old items from database before update
    def delete_items_from_database(self, receipt_id):
        self.cursor.execute('DELETE FROM `receiptitems` WHERE ReceiptID = %s', (receipt_id,))
        self.connection.commit()

    '''
    OCR METHODS
    '''

    # Preprocessing small images
    def preprocess_image(self, image):
        # Load the image

        # Scale the image
        image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blurring to remove noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply Otsu's binarization
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Enhance contrast
        enhanced = cv2.equalizeHist(binary)

        return enhanced

    # Reading text from small images
    def read_text(self, image1):
        # import here bcs on the top program is much slower even when not used ocr
        import easyocr
        image = self.preprocess_image(image1)
        reader = easyocr.Reader(['en'], gpu=False)
        text_detections = reader.readtext(image)
        data = ""
        has_digits = False
        for result in text_detections:
            text = result[1]
            data += text

        # draw_bounding_boxes(img, text_detections, threshold)
        cv2.imwrite('1083-receipt_roi_fixed.png', image)

        return data

    # Preprocessing whole receipt image
    def preprocess_receipt_image(self, file_path):
        image = cv2.imread(file_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (22, 5))
        dilate = cv2.dilate(thresh, kernal, iterations=1)

        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cnts = sorted(cnts, key=lambda x: (cv2.boundingRect(x)[1], cv2.boundingRect(x)[0]))
        results = []
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if h < 100 and w < 300:
                roi = image[y:y + h, x:x + w]
                ocr_result = self.read_text(roi)
                results.append(ocr_result)

        return results

    # Use ML model to look for products in ocr results
    def look_for_products(self, ocr_results):
        with open('ReceiptsPage/AddNewReceipt/MachineLearning/model_product.pkl', "rb") as file:
            loaded_model = load(file)
        with open("ReceiptsPage/AddNewReceipt/MachineLearning/vectorizer_product.pkl", "rb") as file:
            loaded_vectorizer = load(file)

        products_list = []
        for item in ocr_results:
            list = []
            list.append(item)
            ocr_results_vectorized = loaded_vectorizer.transform(list)
            prediction = loaded_model.predict(ocr_results_vectorized)
            if prediction[0] == 1:
                products_list.append(item)

        return products_list

    # Use regex to get prices from ocr results
    def look_for_prices(self, ocr_results):
        price_list = []
        for item in ocr_results:
            if re.search(r'^\d+(?:[.]\d{1,2}|$)$', item) or re.search(r'^\d+(?:[,]\d{1,2}|$)$', item):
                print(item)
                price_list.append(item)
        return price_list

    # Create dict from products and prices lists
    def create_dict(self, products_list, price_list):
        zipped_dict = dict(zip(products_list, price_list))
        return zipped_dict

    # Write dict to dataframe
    def dict_to_df(self, items_dict, items_df):
        data = [(k, v) for k, v in  items_dict.items()]
        df = pd.DataFrame(data, columns=["Item name", "Item price"])
        return df

    '''
    EDIT ELEMENT METHODS
    '''

    def edit_element_in_df(self, items_df, old_name, new_name, new_price):
        row_index = items_df.loc[items_df["Item name"] == old_name].index[0]
        items_df.loc[row_index, 'Item name'] = new_name
        items_df.loc[row_index, "Item price"] = float(new_price)

        return items_df
