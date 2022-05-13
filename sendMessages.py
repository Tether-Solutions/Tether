import email, smtplib, ssl
from providers import PROVIDERS

import time


def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "Hi! It's Crypto Bot!",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)


def priceReportDOWN(ethSMSPercentChangeHourly, ethSMSPrice):
    ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly/100, 2)
    ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly, 2)
    ethSMSPrice = round(ethSMSPrice, 2)

    number = '8042456976'
    messagev2 = "Ethereum has gown down from " + str((1-ethSMSPercentChangeHourly) * ethSMSPrice) + " to " + str(ethSMSPrice) + " in the last hour(" + str(ethSMSPercentChangeHourly) + "%)"
    provider = "T-Mobile"
    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    send_sms_via_email(number, messagev2 , provider, sender_credentials)

    

def priceReportUP(ethSMSPercentChangeHourly, ethSMSPrice):
    ethSMSPercentChangeHourly /= 100
    ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly, 2)
    ethSMSPrice = round(ethSMSPrice, 2)

    number = '8042456976'
    messagev3 = " Ethereum has gone up from " + str((1+ethSMSPercentChangeHourly) * ethSMSPrice) + " to " + str(ethSMSPrice) + " in the last hour the percent change is(" + str(ethSMSPercentChangeHourly) + "%)"
    provider = "T-Mobile"
    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    send_sms_via_email(number, message, provider, sender_credentials)

