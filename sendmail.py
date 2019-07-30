# you need to allo less security app in your gmail setting

import smtplib, ssl

gmail_port = 465
smtp_server = "smtp.gmail.com"
sender = input("Enter your Gmail: ")
password = input("Enter your password: ")
receiver = input("Email to whome you want to send message: ")
message = input("Message to be sent: ")
ctx = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, smtp_server, ctx) as server:
  server.login(sender, password)
  server.sendmail(sender, receiver, message)
  print("mail sent")
