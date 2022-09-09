# Import smtplib and ssl modules
import smtplib, ssl

# Define message parameters
from_email = "your@email.com"
to_email = "their@email.com"
subject = "Test email from Python"
message = "This is a test email from Python."

# Add subject to top of message
message = "Subject: " + subject + "\n\n" + message

# Define mail server parameters
smtp_server = "your.mail.server"
smtp_port = 465

# Get your email password
smtp_pass = input("Please enter your SMTP password: ")

# Create an SSL context
context = ssl.create_default_context()

# Send the mail
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context = context) as smtp_srv:
        smtp_srv.login(from_email, smtp_pass)
        smtp_srv.sendmail(from_email, to_email, message)
except Exception as e:
	# Display details about any error that occurred
	print(e)
