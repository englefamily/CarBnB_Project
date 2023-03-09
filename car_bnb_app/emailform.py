from email.message import EmailMessage
# import smtplib
# 'email.sender298@gmail.com'
# # def send_email(email_receiver='g.hananel20@gmail.com', subject='test', body='body test'):
# email_sender = 'g.hananel20@gmail.com'
# password = 'lxfunwxysulmsivv'
# email_receiver = 'g.hananel22@gmail.com'
#
# subject = 'test'
# body = """
# chacking jhfgdaskjdhsakjdfn dugfjksajdfasfsaf
# """
#
# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)
# # 465
# # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# #     smtp.login(email_sender)
# #     smtp.sendmail(email_sender, email_receiver, em.as_string())
#
# try:
#     connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     connection.ehlo()
#     connection.login(user=email_sender, password=password)
#     connection.sendmail(from_addr=email_sender,
#         to_addrs=email_receiver,
#         msg="Subject:Motivational quote\n\n" + body)
#     connection.close()
#
#     print('Email sent!')
# except Exception as e:
#     print(e)

import smtplib

# Replace with your email address
email_sender = 'info@gelato45ltd.com'
# Replace with your password
password = 'sbekHq*_De*%w7@@_jk2'
# Replace with the email address of the recipient
email_receiver = 'viviengle@gmail.com'

subject = 'Send Email from Python'
body = 'Test email from Python'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

with smtplib.SMTP_SSL('auth.smtp.1and1.co.uk', 465) as smtp:
    smtp.login(email_sender, password=password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

