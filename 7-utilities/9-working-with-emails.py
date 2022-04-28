import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from credentials import credential

message=MIMEMultipart()
message["from"]="Zartab Nakhwa"
message["to"]="nzartab@gmail.com"
message["subject"]="Mail form JP PYthon April 2022 Batch"

body=' Hey There, this is a test message'
message.attach(MIMEText(body))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("codewithz21@gmail.com",credential.get_password())
    smtp.send_message(message)
    print("Sent...")
