# Budget-management-app
# Budget Management Application

Welcome to the Budget Management Application! This app is designed to help users efficiently manage their finances by providing tools for budgeting, expense tracking, savings goals, and more. Built primarily with Python and MySQL, this application aims to simplify financial management for everyone.

## Features

### User Authentication
- **Login Page**: Secure login with options to show/hide password and a "Forgot Password" feature that sends a password reset email.
- **Account Creation**: Easy account setup for new users.

### Budget Management
- **Manage Budgets**: Create monthly budgets up to one year in advance. 
- **Automatic Updates**: Add constant expenses and incomes that automatically update future budgets.
- **Budget Overview**: View a summary of income, expenses, and remaining balance.

### User Engagement
- **Rate the App**: Users can rate the application on a scale from 1 to 5.
- **Questionnaire**: Fill out a form to provide feedback and personal details for future analysis.

### Receipts Management
- **Add Receipts**: Users can manually input receipts or upload photos for OCR processing (currently under improvement).

### Savings Goals
- **Set Goals**: Define savings goals with options to deposit or withdraw funds.
- **Automatic Deposits**: Schedule automatic deposits on the first day of each month.
- **Progress Tracking**: Monitor progress towards savings goals.
- **Investment & Deposit Calculators**: Tools for calculating potential investment returns and bank deposit interests.

### Additional Features
- **Settings Page**: Customize app preferences (e.g., dark mode), view app information, and access support.
- **Shopping List**: Create organized checklists for shopping trips.
- **Statistics Page**: Analyze spending and income trends using graphs and timelines.
- **Account Management**: Clear data, delete accounts, change passwords, verify emails, and manage email notifications.

## Technologies Used
- Python
- MySQL
- Optical Character Recognition (OCR)
- Machine Learning (ML)

## Installation

To set up the Budget Management Application locally, follow these steps:

1. **Clone the Repository**
2. **Install Dependencies**
   Make sure you have Python installed. Then install the required packages:
   
   pip install -r requirements.txt
   
4. **Set Up MySQL Database**
  - Create a MySQL database for the application. (On Localhost)
4. **Restore Database from Dump File**
  If you have a dump file, restore it by running:

  mysql -u [username] -p [database_name] < [dumpfilename.sql]
  
  ( database name: budgetappdatabse, username: replace with your username, dumpfiles: in "Database set up" folder)
5. **Run the Application**
  Execute the main application file:
  -RunApp.py

