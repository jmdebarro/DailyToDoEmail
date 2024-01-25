import smtplib, goals, login
from email.message import EmailMessage

daily_goals = goals.Goals()
email_content = f"Today's Tasks\n1. {daily_goals.one}\n2. {daily_goals.two}\n3. {daily_goals.three}\n4. {daily_goals.four}"

# Create message object
msg = EmailMessage()
msg.set_content(email_content)

# Initialize msg object
msg['Subject'] = "Daily To-Do"
msg['From'] = login.EMAIL
msg['To'] = "jmdebarro@gmail.com"

s = smtplib.SMTP("smtp.office365.com", port=587)
s.starttls()
s.login(login.EMAIL, login.PASS)
s.send_message(msg)
s.quit()
