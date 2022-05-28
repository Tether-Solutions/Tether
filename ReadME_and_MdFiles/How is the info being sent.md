# How is the info being sent?

Aaryan Asthana 

Sending Messages to the Phone:

<aside>
💡 A significant part of this solution is credited to a [tutorial we found on YouTube](https://www.youtube.com/watch?v=4-ysecoraKo&ab_channel=AlfredoSequeida) by Alfredo Sequida. In this guide, I explain what the code does and the new functions that we added.

</aside>

# Background:

Before I get started on how text messages are sent to your phone, I wanted to provide some foundational info. First, let’s get on the same page with the terms. SMS, or short messaging service, is what a text message is; which is limited to 160 characters and sent over mobile networks. Now, there are many platforms, such as Twilio, that allow you to send text messages programmatically using their API. However, these alternatives almost always come with a fee. After doing some research, we found out that a possible method to send text messages for free is by utilizing email. 

# Sending SMS Messages:

To send free text messages, what we'll be doing is using SMS gateways, which are servers that serve as middlemen and can be used to deliver our messages to mobile phones via mobile networks. Unlike Twilio, these SMS gateways can be used for free because one of the ways we can interact with them is by using email. Basically, these gateways which the mobile providers have set up allow us to send our text messages in the form of an email message, and then forward our messages to mobile phones via SMS.

In our providers.py file, we have the list of the majority of SMS Domains for U.S phone providers. This code was given to us by the tutorial. (Complete file not shown) :

```python
PROVIDERS = {
    "AT&T": {"sms": "txt.att.net", "mms": "mms.att.net", "mms_support": True},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "mms": "myboostmobile.com",
        "mms_support": True,
    },
    "Cricket Wireless": {
        "sms": "sms.cricketwireless.net ",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
    },
    "Metro PCS": {"sms": "mymetropcs.com", "mms_support": True},
    "Mint Mobile": {"sms": "mailmymobile.net", "mms_support": False},
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "mms_support": False,
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "mms": "pm.sprint.com",
        "mms_support": True,
    }
```

Now, other than having these email domains for the different providers, we also needed to have an email provider which gave us access to the SMTP (**Simple Mail Transfer Protocol)** servers. In our case, we used Gmail’s SMTP server. In order to do this, we created a new Gmail account and set up an **app password.** Essentially, an app password is a key that serves as a way to log in and is a 16-digit passcode that gives an app or device **restricted access to your Google Account** without having to use your personal password to get complete access to your Google Account

# The Code:

Let’s get to the code. The first thing we have to do is import some modules. We will be using `email`to format the emails later. We also need the `smtp` library which will send the messages through SMTP servers. We also need `SSL`and we'll be using that as our connection with the SMTP servers. And then, one more thing we're going to add is the providers files from before.

```python
import email, smtplib, ssl
from providers import PROVIDERS
```

Now, we can make the function that sends the SMS via email, which has quite a few parameters:

```python
def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "Hello, Its Crypto Bot!",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
```

The first one is number, which is simply the number we’ll be sending these emails to. We also need the message we are sending, which will be of type string. Next, we will use the provider, also of type string, to serve as the carrier. This carrier will correspond with one of the providers in [providers.py](How%20is%20the%20info%20being%20sent%2027ce41549dec47d69a33b7db8d091e4c.md) Next, we need the sender credentials. This includes the email and the app password from earlier. The subject is necessary for emails, and will be a string. Next is the parameter for the SMTP server. In this case, we’re using Gmail, so the default for that is `smtp.gmail.com` One last thing we need is the port that's going to be used to send these emails.