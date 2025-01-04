import mysql.connector


class QuestionnaireWindowsModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

    def get_questions_with_answers(self):
        self.questions_with_answers = {
            "What is your full name?": {
                "type": "short_entry",
                "answers": None
            },
            "What is your gender?": {
                "type": "select_4",
                "answers": [
                    "Male",
                    "Female",
                    "Non-binary",
                    "Prefer not to say"
                ]
            },
            "Which country are you from?": {
                "type": "short_entry",
                "answers": None
            },
            "What is your level of education?": {
                "type": "select_4",
                "answers": [
                    "High School",
                    "Bachelor's Degree",
                    "Master's Degree",
                    "Doctorate"
                ]
            },
            "What is your marital status? (e.g., married, single, etc.)": {
                "type": "select_4",
                "answers": [
                    "Married",
                    "Single",
                    "Divorced",
                    "Widowed"
                ]
            },
            "How would you describe your health condition?": {
                "type": "select_4",
                "answers": [
                    "Excellent",
                    "Good",
                    "Fair",
                    "Poor"
                ]
            },
            "Do you live in a big city or a small city?": {
                "type": "select_4",
                "answers": [
                    "Big City",
                    "Small City",
                    "Town",
                    "Rural Area"
                ]
            },
            "What is your gross monthly salary range?": {
                "type": "select_4",
                "answers": [
                    "$0 - $2,000",
                    "$2,001 - $5,000",
                    "$5,001 - $10,000",
                    "$10,001 and above"
                ]
            },
            # Continuing with the remaining questions
            "Do you have a credit card?": {
                "type": "select_2",
                "answers": [
                    "Yes",
                    "No"
                ]
            },
            "Do you have any consumer credits?": {
                "type": "select_2",
                "answers": [
                    "Yes",
                    "No"
                ]
            },
            "Do you have any house credit?": {
                "type": "select_2",
                "answers": [
                    "Yes",
                    "No"
                ]
            },
            # Additional questions
            "Are you satisfied with the financial level of your life?": {
                "type": "select_4",
                "answers": [
                    "Very Satisfied",
                    "Satisfied",
                    "Neutral",
                    "Dissatisfied"
                ]
            },
            # Travel frequency questions
            "How often do you travel abroad for relaxation?": {
                "type": "select_4",
                "answers": [
                    "Never",
                    "Once a year",
                    "Several times a year",
                    "Monthly"
                ]
            },
            # Domestic travel frequency question
            "How often do you travel within your country for relaxation?": {
                "type": "select_4",
                "answers": [
                    "Never",
                    "Once a year",
                    "Several times a year",
                    "Monthly"
                ]
            },
            # Online shopping frequency question
            "How often do you buy things online?": {
                "type": "select_4",
                'answers': [
                    'Never',
                    'Rarely (once a month)',
                    'Often (once a week)',
                    'Very Often (multiple times a week)'
                ]
            },
            # Social media scrolling frequency question
            'How often do you scroll through social media?': {
                'type': 'select_4',
                'answers': [
                    'Never',
                    'A few times a week',
                    'Daily',
                    'Multiple times a day'
                ]
            },
            # Drinking frequency question
            'How often do you drink alcohol?': {
                'type': 'select_4',
                'answers': [
                    'Never',
                    'Occasionally (social events)',
                    'Regularly (a few times a week)',
                    'Daily'
                ]
            },
            # Smoking frequency question
            'How often do you smoke?': {
                'type': 'select_4',
                'answers': [
                    'Never',
                    'Occasionally (social events)',
                    'Regularly (a few times a week)',
                    'Daily'
                ]
            },
            # Savings goal question
            'How much would you like to save yearly?': {
                'type': 'short_entry',
                'answers': None
            },
            # Monthly income goal question
            'How much would you like to earn per month?': {
                'type': 'short_entry',
                'answers': None
            },
            # App discovery source question
            'How did you hear about this app?': {
                'type': 'long_entry',
                'answers': None
            },
            # Improvement suggestions question
            'Are there any improvements you would suggest so far?': {
                'type': 'long_entry',
                'answers': None
            },
            # Most used functionality question
            'What functionality do you use the most?': {
                'type': 'long_entry',
                'answers': None
            }
        }
        return self.questions_with_answers

    def get_type_and_answers(self, question):
        if question in self.questions_with_answers:
            question_details = self.questions_with_answers[question]
            question_type = question_details["type"]
            question_answers = question_details["answers"] if question_details["answers"] is not None else None
            return question_type, question_answers
        else:
            return None, None  # Return None for both if key is not found


        # Toggle selected checkbutton and update its value in list

    @staticmethod
    def toggle_checkbutton(index: int, check_vars: list) -> list:
        for i, var in enumerate(check_vars):
            if i == index:
                if check_vars[i]:
                    check_vars[i] = False
                    break

                check_vars[i] = True
        print(check_vars)
        return check_vars

    def look_for_true(self, check_list):
        print(check_list)
        count = 0
        index = None
        for i in range(len(check_list)):
            if check_list[i]:  # Check if the current element is True
                count += 1
                index = i

        if count == 1:
            return index  # Return the index of the single True value
        return "Error"  # Return "Error" if there are none or more than one True values


    def insert_data_to_database(self, user_data, user_answers):
        # SQL Insert query
        insert_query = """
                        INSERT INTO UserQuestionnaire (
                            username, Email, full_name, gender, country, education_level,
                            marital_status, health_condition, city_size, salary_range,
                            credit_card, consumer_credits, house_credit,
                            financial_satisfaction, travel_abroad_frequency,
                            travel_within_country_frequency, online_shopping_frequency,
                            social_media_frequency, alcohol_consumption_frequency,
                            smoking_frequency, yearly_savings_goal,
                            monthly_income_goal, app_discovery_source,
                            improvement_suggestions, most_used_functionality
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                  %s, %s, %s, %s, %s);
                        """
        data_to_insert = [user_data[0], user_data[1]] + user_answers

        self.cursor.execute(insert_query, data_to_insert)
        self.connection.commit()  # Commit the transaction


    def update_data_in_database(self, user_data, user_answers):
        # SQL Update query
        update_query = """
                        UPDATE UserQuestionnaire
                        SET 
                            full_name = %s,
                            gender = %s,
                            country = %s,
                            education_level = %s,
                            marital_status = %s,
                            health_condition = %s,
                            city_size = %s,
                            salary_range = %s,
                            credit_card = %s,
                            consumer_credits = %s,
                            house_credit = %s,
                            financial_satisfaction = %s,
                            travel_abroad_frequency = %s,
                            travel_within_country_frequency = %s,
                            online_shopping_frequency = %s,
                            social_media_frequency = %s,
                            alcohol_consumption_frequency = %s,
                            smoking_frequency = %s,
                            yearly_savings_goal = %s,
                            monthly_income_goal = %s,
                            app_discovery_source = %s,
                            improvement_suggestions = %s,
                            most_used_functionality = %s
                        WHERE username = %s AND Email = %s;
                        """
        data_to_update = user_answers + [user_data[0], user_data[1]]  # Append username and email

        # Execute the update query with the combined data
        self.cursor.execute(update_query, data_to_update)
        self.connection.commit()  # Commit the transaction

    def get_questionnaire_info(self, user_data):
        select_query = "SELECT COUNT(*) FROM UserQuestionnaire WHERE username = %s;"

        # Execute the select query
        self.cursor.execute(select_query, (user_data[0],))
        result = self.cursor.fetchone()  # Fetch the result

        # Check if any record exists
        return result[0] > 0  # Returns True if count > 0, else False
