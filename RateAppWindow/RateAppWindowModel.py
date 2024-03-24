import mysql.connector


class RateAppWindowsModel:
    def __init__(self):
        # Connecting to MySQL database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()
        self.user_rating_from_db = ""

    # Check if user has already rated the app
    def check_if_has_already_rated_app(self, user_data):
        username = user_data[0]
        self.cursor.execute("SELECT * FROM `rating` WHERE user_login = %s", (username,))
        row = self.cursor.fetchone()
        if row is None:
            # User has not rated app
            return True
        # User has already rated app
        self.user_rating_from_db = row[1]
        return False

    # Check if user choose nuber of stars
    def check_if_user_choose(self, final_rating):
        if final_rating == "":
            return False
        return True

    # Update user rating
    def update_user_rating(self, user_data, user_rating):
        self.cursor.execute('UPDATE budgetappdatabase.rating SET user_rating = %s WHERE user_login = %s',
                            (user_rating, user_data[0]))
        self.connection.commit()

    # Insert user rating
    def insert_user_rating(self, user_data, user_rating):
        insert_rating = 'INSERT INTO `rating` (user_login, user_rating) VALUES (%s, %s)'
        values_to_insert = (user_data[0], user_rating)
        self.cursor.execute(insert_rating, values_to_insert)
        self.connection.commit()
