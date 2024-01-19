import smtplib, goals
from email.message import EmailMessage

daily_goals = goals.Goals()
email_content = ""

# Create message object
msg = EmailMessage()

# Initialize msg object
msg['Subject'] = email_content
msg['From'] = "jmdebarro2@gmail.com"
msg['To'] = "jmdebarro@gmail.com"

s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()
