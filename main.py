import smtplib
import os
from dotenv import load_dotenv

# To get this program to work and send an email
# Install the python-dotenv library and create a .env file
#       (remember to add the .env file to your .gitignore so no sensitive info is available online)
#   Create 4 env variables (FROM_PASSWORD, APP_PASSWORD, RECIPIENT, SMTP_ADDRESS) and fill them in with the
#  appropriate info
# ex. SMTP_ADDRESS=smtp.gmail.com

# NOTE: Gmail requires separate app passwords for any third party app sending emails.
# First step is to add two step verification and then create an app password from the Security tab
# That app password will be what is used in connection.login to send the password

# env variables
load_dotenv()
email_address = os.getenv("FROM_EMAIL")
email_password = os.getenv("APP_PASSWORD")
recipient = os.getenv("RECIPIENT")
smtp_info = os.getenv("SMTP_ADDRESS")

# Change these to create your desired message
subject_line = "Hello"
email_body = "Hello, World\nHow are you today?"

# email connection
with smtplib.SMTP(smtp_info) as connection:
    # starttls encrypts connection
    connection.starttls()
    connection.login(user=email_address, password=email_password)
    connection.sendmail(from_addr=email_address,
                        to_addrs=recipient,
                        msg=f"Subject:{subject_line}\n\n{email_body}")

