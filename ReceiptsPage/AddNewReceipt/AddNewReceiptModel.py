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
    @staticmethod
    def create_df():
        items_df = pd.DataFrame(columns=["Item name", "Item price"])
        return items_df

    # Adding items to dataframe
    @staticmethod
    def add_items_to_df(item_name: str, item_price: str, items_df):
        new_row = {"Item name": item_name, "Item price": item_price}
        new_df = pd.DataFrame([new_row], index=[len(items_df)])
        updated_df = pd.concat([items_df, new_df], ignore_index=False)
        return updated_df

    # Delete selected item from dataframe
    @staticmethod
    def delete_from_df(item_name: str, items_df):
        items_df.drop(items_df[items_df['Item name'] == item_name].index, inplace=True)
        items_df = items_df.reset_index(drop=True)
        return items_df

    # Choose file to photo via filedialog
    @staticmethod
    def choose_file() -> str:
        filepath = filedialog.askopenfilename()
        return filepath

    # Counts number of items in receipt
    @staticmethod
    def item_count_in_receipt(items_df) -> int:
        num_rows = len(items_df.index)
        return num_rows

    # Calculates total price of receipt
    @staticmethod
    def calculate_total_price(items_df) -> float:
        prices = items_df['Item price'].tolist()
        total = 0
        for price in prices:
            total += float(price)
        return total

    # Adding receipt to database
    def add_receipt_to_database(self, user_data: tuple, receipt_name: str, item_count: int, creation_date):
        insert_query = 'INSERT INTO `receipts` (UserName, ReceiptName, ItemsCount, CreationDate)' \
                       ' VALUES (%s, %s, %s, %s)'
        values_to_insert = (user_data[0], receipt_name, str(item_count), creation_date)
        self.cursor.execute(insert_query, values_to_insert)
        self.connection.commit()

    # Gets receipt id from database
    def get_receipt_id(self, receipt_name: str) -> int:
        self.cursor.execute('SELECT ReceiptID FROM `receipts` WHERE ReceiptName = %s', (receipt_name,))
        row = self.cursor.fetchone()
        receipt_id = row[0]
        return receipt_id

    # Adding items from receipt to database and assign it to receipt id
    def add_items_to_database(self, receipt_id: int, user_data: tuple, items_df, total: float):
        for index, row in items_df.iterrows():
            item, price = self.get_items_and_prices(row)
            insert_query = 'INSERT INTO `receiptitems` (ReceiptID, Username, Item, Price, TotalPrice)' \
                           ' VALUES (%s, %s, %s, %s, %s)'
            values_to_insert = (receipt_id, user_data[0], item, price, total)
            self.cursor.execute(insert_query, values_to_insert)
            self.connection.commit()

    # Get time of receipt creation in system
    @staticmethod
    def get_creation_time():
        creation_date = date.today()
        return creation_date

    # Gets item name and its price
    @staticmethod
    def get_items_and_prices(row) -> tuple:
        name = row["Item name"]
        price = row["Item price"]

        return name, price

    # Check if receipt name is unique
    @staticmethod
    def check_for_duplicates(receipt_name: str, list_of_user_receipts: list) -> bool:
        for receipt in list_of_user_receipts:
            if receipt == receipt_name:
                return True
        return False

    '''
    UPDATE METHODS
    '''

    # Updates item count
    def update_item_count(self, item_count: int, receipt_id: int):
        self.cursor.execute('UPDATE `receipts` SET ItemsCount = %s WHERE ReceiptID = %s', (item_count, receipt_id))
        self.connection.commit()

    # Delete old items from database before update
    def delete_items_from_database(self, receipt_id: int):
        self.cursor.execute('DELETE FROM `receiptitems` WHERE ReceiptID = %s', (receipt_id,))
        self.connection.commit()

    '''
    OCR METHODS
    '''

    # Preprocessing small images
    @staticmethod
    def preprocess_image(image):
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
    def read_text(self, image1) -> str:
        # import here bcs on the top program is much slower even when not used ocr
        import easyocr
        image = self.preprocess_image(image1)
        reader = easyocr.Reader(['en'], gpu=False)
        text_detections = reader.readtext(image)
        data = ""

        for result in text_detections:
            text = result[1]
            data += text

        # draw_bounding_boxes(img, text_detections, threshold)
        cv2.imwrite('1083-receipt_roi_fixed.png', image)

        return data

    # Preprocessing whole receipt image
    def preprocess_receipt_image(self, file_path: str) -> list:
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
    @staticmethod
    def look_for_products(ocr_results: list) -> list:
        with open('ReceiptsPage/AddNewReceipt/MachineLearning/model_product.pkl', "rb") as file:
            loaded_model = load(file)
        with open("ReceiptsPage/AddNewReceipt/MachineLearning/vectorizer_product.pkl", "rb") as file:
            loaded_vectorizer = load(file)

        products_list = []
        for item in ocr_results:
            p_list = [item]
            ocr_results_vectorized = loaded_vectorizer.transform(p_list)
            prediction = loaded_model.predict(ocr_results_vectorized)
            if prediction[0] == 1:
                products_list.append(item)

        return products_list

    # Use regex to get prices from ocr results
    @staticmethod
    def look_for_prices(ocr_results: list) -> list:
        price_list = []
        for item in ocr_results:
            if re.search(r'^\d+(?:[.]\d{1,2}|$)$', item) or re.search(r'^\d+(?:[,]\d{1,2}|$)$', item):
                print(item)
                price_list.append(item)
        return price_list

    # Create dict from products and prices lists
    @staticmethod
    def create_dict(products_list: list, price_list: list) -> dict:
        zipped_dict = dict(zip(products_list, price_list))
        return zipped_dict

    # Write dict to dataframe
    @staticmethod
    def dict_to_df(items_dict: dict):
        data = [(k, v) for k, v in items_dict.items()]
        df = pd.DataFrame(data, columns=["Item name", "Item price"])
        return df

    '''
    EDIT ELEMENT METHODS
    '''

    @staticmethod
    def edit_element_in_df(items_df, old_name: str, new_name: str, new_price: float):
        row_index = items_df.loc[items_df["Item name"] == old_name].index[0]
        items_df.loc[row_index, 'Item name'] = new_name
        items_df.loc[row_index, "Item price"] = float(new_price)

        return items_df
