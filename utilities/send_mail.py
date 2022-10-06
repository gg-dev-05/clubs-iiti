
def send_mail(receiver_email, message):
    return True
    # print("Sending mail to " + receiver_email)
    # print(message)
    # context = ssl.create_default_context()

    # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)