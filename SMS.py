import email, smtplib, ssl
from providers import PROVIDERS
import API

ethSMSPrice = API.ethPriceReport()['priceETH']
ethSMSPrice = round(ethSMSPrice, 2)
ethSMSPercentChangeDaily = API.ethPriceReport()['percentChangeDAILY']
ethSMSPercentChangeDaily = round(ethSMSPercentChangeDaily, 2)
ethSMSPercentChangeHourly = API.ethPriceReport()['percentChangeHRLY']
ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly, 2)

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
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



def main():
    number = "8045479964"
    message = "The Etherium price is " + str(ethSMSPrice) + " , It Has gone up " + str(ethSMSPercentChangeDaily) + " percent in the last day"
    provider = "T-Mobile"

    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")



    send_sms_via_email(number, message, provider, sender_credentials)

def priceReportDOWN():
    number = '8045479964'
    message = "Etherium has gown down from" + str((1+ethSMSPercentChangeHourly) * ethSMSPrice) + " to " + str(ethSMSPrice) + " in the last hour(" + str(ethSMSPercentChangeHourly) + ")"
    provider = "T-Mobile"

    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == "__main__":

    main()
    priceReportDOWN()