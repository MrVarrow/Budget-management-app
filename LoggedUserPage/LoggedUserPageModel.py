import mysql.connector
from datetime import datetime, timedelta


class LoggedUserPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Get today's date
    @staticmethod
    def get_today_date():
        today = datetime.now()
        today = datetime.date(today)

        return today

    def count_1st_days_between_months(self, date_1, date_2):
        if date_1 > date_2:
            date_1, date_2 = date_2, date_1

            # Initialize count of first days
        count = 0

        if date_1.day != 1:
            current_date = date_1.replace(day=1) + timedelta(days=31)  # Move to next month
            current_date = current_date.replace(day=1)  # Set to first day of next month
        else:
            current_date = date_1

            # Loop until we exceed date_2
        while current_date <= date_2:
            count += 1  # Count the first day of the month
                # Move to the first day of the next month
            if current_date.month == 12:  # December case
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

        return count

    def get_last_login_date(self, user_data: tuple):
        self.cursor.execute('SELECT lastseen FROM user WHERE username = %s',
                            (user_data[0]))

    def get_user_goals_list(self):
        ...


    def count_amount_added_to_goal(self):
        ...

    def update_amount_in_goal(self):
        ...


