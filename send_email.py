import smtplib, ssl
import os

def send_email(message, from_email):
    host = 'smtp.gmail.com'
    port = 465

    username = "scarrier99@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")

    receiver = "scarrier99@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)