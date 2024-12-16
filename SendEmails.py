import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, subject, message):
    global server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)  # You can omit this line
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
    finally:
        server.quit()


def send_confirm_email(email_input):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(email_input)
    subject = 'Thanks for Registration!'
    message = 'Your Registration to BudgetApp went successfully, now you can login to your account.'

    send_email(sender_email, sender_password, receiver_email, subject, message)


def forgot_password_email(receiver, password):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Did you forget your password?'
    message = 'Here is your password to budget app:\n' \
              '{}'.format(password)

    send_email(sender_email, sender_password, receiver_email, subject, message)


def send_email_with_link(receiver, link):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Did you forget your password?'
    message = 'Here is your link to download mobile app:\n' \
              '{}'.format(link)

    send_email(sender_email, sender_password, receiver_email, subject, message)


def send_email_with_code(receiver, code):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Did you forget your password?'
    message = 'Here is your code to verify your e-mail:\n' \
              '{}'.format(code)

    send_email(sender_email, sender_password, receiver_email, subject, message)

# to impelent
def send_email_with_email_change_info(receiver, username, new_email):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'E-mail changed.'
    message = 'You had changed your E-mail for account {} to\n' \
              '{}'.format(username, new_email)

    send_email(sender_email, sender_password, receiver_email, subject, message)
# to impelent
def send_email_with_delete_acc(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Account Deleted.'
    message = 'You had deleted your account with username\n' \
              '{}, if you want you can tell us why did you decided to do so in reply to this E-mail. Thanks!'.format(username)

    send_email(sender_email, sender_password, receiver_email, subject, message)

# to impelent
def send_email_with_clear_data(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'All data from your account has been cleaned.'
    message = 'You had cleaned data from your account with username\n' \
              '{}, if you want you can tell us why did you decided to do so in reply to this E-mail. Thanks!'.format(
        username)

    send_email(sender_email, sender_password, receiver_email, subject, message)


# OPTIONAL

# to impelent
def send_email_when_saving_goal_full(receiver, goal_name):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Good job! Your goal is full.'
    message = 'Your goal: {} is full make sure to withdraw money and set new goals.'.format(goal_name)

    send_email(sender_email, sender_password, receiver_email, subject, message)
# to impelent
def send_email_to_rate_the_app(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Rate budget app.'
    message = 'Hi, {} We will be glad if you would like to rate our app, you can do this directly in app by clicking' \
              'rate app button in main menu. Thanks!'.format(username)

    send_email(sender_email, sender_password, receiver_email, subject, message)

# to impelent
def send_email_thanks_for_rate(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'We want to thank you for your time.'
    message = 'Hi, {} thanks for rating our app!'.format(username)

    send_email(sender_email, sender_password, receiver_email, subject, message)
# to impelent
def send_email_when_user_was_inactive(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'We got some news for you in budget app'
    message = 'Hi, {}!\n We havent seen each other for a long time. We miss you :( Come back and see whats new' \
              'in the app and keep tracking your finances.'.format(username)

    send_email(sender_email, sender_password, receiver_email, subject, message)
# to impelent
def send_email_with_reminder_to_set_budget(receiver, username):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Dont miss your budget for incoming month!'
    message = 'Hi, {} remember to set budget for next month. Dont let your finances take control ' \
              'over you'.format(username)

    send_email(sender_email, sender_password, receiver_email, subject, message)

