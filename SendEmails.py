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


def send_confirm_email(self):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(self.email.get())
    subject = 'Thanks for Registration!'
    message = 'Your Registration to BudgetApp went successfully, now you can login to your account.'

    send_email(sender_email, sender_password, receiver_email, subject, message)


def send_email_verification(self, receiver, code):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'E-mail verification'
    message = 'To verify your e-mail type this code into app:\n' \
              '{}'.format(code)

    send_email(sender_email, sender_password, receiver_email, subject, message)


def forgot_password_email(self, receiver, password):
    sender_email = 'budgetappofficial@gmail.com'
    sender_password = ''  # for safety reasons leaving empty
    receiver_email = '{}'.format(receiver)
    subject = 'Did you forget your password?'
    message = 'Here is your password to budget app:\n' \
              '{}'.format(password)

    send_email(sender_email, sender_password, receiver_email, subject, message)
