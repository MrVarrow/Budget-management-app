import mysql.connector


class RateAppWindowsModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        self.user_rating_from_db = ""

    # Check if user has already rated the app
    def check_if_has_already_rated_app(self, user_data: tuple) -> bool:
        username = user_data[0]
        self.cursor.execute("SELECT rating FROM `user` WHERE username = %s", (username,))
        row = self.cursor.fetchone()
        if row[0] == '0':
            # User has not rated app
            return True
        # User has already rated app
        self.user_rating_from_db = row[0]
        return False

    # Check if user choose nuber of stars
    @staticmethod
    def check_if_user_choose(final_rating: str) -> bool:
        if final_rating == "":
            return False
        return True

    # Update user rating
    def update_user_rating(self, user_data: tuple, user_rating: str):
        self.cursor.execute('UPDATE budgetappdatabase.user SET rating = %s WHERE username = %s',
                            (user_rating, user_data[0]))
        self.connection.commit()

    # Insert user rating
    def insert_user_rating(self, user_rating: str):
        insert_rating = 'INSERT INTO `rating` (user_rating) VALUES (%s)'
        values_to_insert = user_rating
        self.cursor.execute(insert_rating, values_to_insert)
        self.connection.commit()
