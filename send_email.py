import smtplib, ssl


def send_email(message, from_email):
    host = 'smtp.gmail.com'
    port = 465

    username = "scarrier99@gmail.com"
    password = "iqah exep rcws prxv"

    receiver = "scarrier99@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)