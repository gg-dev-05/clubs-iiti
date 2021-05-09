import os

'''
Configuration for sending emails
'''

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.environ.get("mail_id")
password = os.environ.get("mail_password") 