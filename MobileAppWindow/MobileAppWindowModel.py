import mysql.connector
import pyperclip
from SendEmails import send_email_with_link


class MobileAppWindowsModel:
    def __init__(self):
        # Connecting to MySQL local database
        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="AkniLUAp01-",
                                                  database="budgetappdatabase")
        self.cursor = self.connection.cursor()

        self.user_info = {
            "full_name": "",
            "gender": "",
            "country": "",
            "education": "",
            "status": "",
            "health_condition": "",
            "city_size": "",  # BIG/ SMALL CITY
            "monthly_salary_range": "",
            "has_credit_card": "",
            "has_consumer_credits": "",
            "has_house_credit": "",
            "financial_satisfaction": "",
            "travel_abroad_frequency": "",
            "travel_domestic_frequency": "",
            "online_shopping_frequency": "",
            "social_media_scrolling_frequency": "",
            "drinking_frequency": "",
            "smoking_frequency": "",
            "yearly_savings_goal": "",
            "monthly_income_goal": "",
            "app_discovery_source": "",
            "improvement_suggestions": "",
            "most_used_functionality": ""
        }

    def get_questions_with_answers(self):
        questions_with_answers = {
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
        return questions_with_answers


    # Copy link to the app to clipboard
    def copy_app_link(self, link):
        pyperclip.copy(link)

    # Sends e-mail with link do download the app to user
    def send_email_with_link(self, link, receiver):
        send_email_with_link(receiver, link)


    def save_answer_to_list(self):
        ...
