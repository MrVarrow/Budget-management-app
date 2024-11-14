import mysql.connector
from datetime import timedelta, date


class LoggedUserPageModel:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    # Get today's date
    @staticmethod
    def get_today_date():
        today = date.today()
        return today
    # check case if its first day month and last seen is also first date
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
                            (user_data[0],))
        row = self.cursor.fetchone()
        self.cursor.reset()
        self.connection.commit()
        return row[0]

    def get_user_goals_list(self, user_data):

        self.cursor.execute('SELECT GoalName FROM savingsgoals WHERE username = %s', (user_data[0],))
        rows = self.cursor.fetchall()
        goals = list(rows)
        self.cursor.reset()
        self.connection.commit()

        return goals

    def count_amount_added_to_goal(self, progress, auto_deposit, count):
        if not count == 0:
            new_progress = progress + (auto_deposit * count)
            return new_progress
        else:
            return progress

    def update_amount_in_goal(self, new_progress, user_data, goal_name):
        self.cursor.execute('UPDATE savingsgoals SET Progress = %s WHERE username = %s AND GoalName = %s',
                            (new_progress, user_data[0], goal_name))
        self.connection.commit()

# Get info about goal with given name from database
    def get_info_about_goal(self, user_data, goal_name):
        goal_info = []
        self.cursor.execute('SELECT * FROM savingsgoals WHERE username = %s AND GoalName = %s',
                            (user_data[0], goal_name))
        row = self.cursor.fetchone()
        if row is not None:
            goal_info = list(row)
        return goal_info

    def update_last_seen(self, user_data, today):
        self.cursor.execute('UPDATE user SET lastseen = %s WHERE username = %s',
                            (today, user_data[0]))
        self.connection.commit()
