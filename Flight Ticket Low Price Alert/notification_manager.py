import smtplib

from twilio.rest import Client
import os


Account_SID=os.environ["Account_SID"]
Auth_Token=os.environ["Auth_Token"]

client = Client(Account_SID, Auth_Token)  #twilio client

EMAIL_PROVIDER_SMTP_ADDRESS="EMAIL_PROVIDER_SMTP_ADDRESS"
MY_EMAIL="MY_EMAIL"
MY_PASSWORD="MY_PASSWORD"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_msg(self,body,from_,to):
        message = client.messages.create(
            body=body,
            from_=from_,
            to=to
        )

        print(message.sid)

    def send_emails(self,emails,message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )





