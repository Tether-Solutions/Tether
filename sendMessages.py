#Aaryan Asthana 

import email, smtplib, ssl
from providers import PROVIDERS
import time
from API2 import ethPriceReport

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "Hi! Its Crypto Bot!",
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



def priceReportDOWN(ethSMSPercentChangeHourly, currentPrice, number): #Sends message detailing the negative percent change in ETH price
    temp = ethPriceReport()['percentChangeHRLY']
    temp = round(temp, 4)
    ethSMSPercentChangeHourly /= 100 # Converting whole number into decimal
    ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly, 5) #Round the percent change to two decimal places 
    currentPrice = round(currentPrice, 3) # round current price 

    previousHourPrice = 1+abs(ethSMSPercentChangeHourly)

    ch = previousHourPrice * currentPrice
    ch = round(ch,4)
  
    message = "Ethereum has gone down from " + str(ch) + " to " + str(currentPrice) + " in the last hour (" + str(temp) + "%)"

    provider = "T-Mobile"
  
    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    send_sms_via_email(number, message, provider, sender_credentials)

    


def priceReportUP(ethSMSPercentChangeHourly, currentPrice, number): #Sends message detailing the positive percent change in ETH price

    temp = ethPriceReport()['percentChangeHRLY']
    temp = round(temp,4)
    ethSMSPercentChangeHourly /= 100 # Converting whole number into decimal
    ethSMSPercentChangeHourly = round(ethSMSPercentChangeHourly, 5) #Round the percent change to two decimal
    currentPrice = round(currentPrice, 3)

    previousHourPrice = round(1-ethSMSPercentChangeHourly, 2)

    ch = previousHourPrice * currentPrice
    ch = round(ch, 4)
  
    message = "Ethereum has gone up from " + str(ch) + " to " + str(currentPrice) + " in the last hour (" + str(temp) + "%)"

    provider = "T-Mobile"
    
    sender_credentials = ("cryptoanalyzerapikey@gmail.com", "nrcdalqekjkujvxp")

    send_sms_via_email(number, message, provider, sender_credentials)



