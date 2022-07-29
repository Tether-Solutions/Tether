# Tether

Cryptocurrency Analyzer by Aaryan Asthana and Yuvanesh Anand 

## Guides & Processes

---

[Where is the information coming from?](#Where is the information coming from?)

[How is the info being sent?](#How-is-the-info-being-sent?)

---

## Links

---

https://github.com/Yuvanesh-ux/Tether

[**API**](https://coinmarketcap.com/api/documentation/v1/)

---

# Where is the information coming from?

Yuvanesh Anand

Getting Started on sending ETH Reports to Your Phone

# What needs to be done?

There are a couple steps needed to get ETH(and hopefully other currency) reports sent to your phone. We need to pull the information from [CoinMarketCap](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical)’s API, and package that information in a sensible, easy to read package over text. 

# Where is the info coming from?

## The Setup

We use API.py to access information from CoinMarketCap’s database

But before pulling the data, we need to set some information up to easily access the API every time

```python
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest' 

#The URL variable stores the access point for the API

parameters = {
    'symbol' : 'ETH', 
    'convert' : 'USD' 
}

#Here we store some neccessary information that CoinMarketCap requires to acess its API, such as the currency pair we are trying to access the info for

headers = {
    'Accepts' : 'application/json', 
    'X-CMC_PRO_API_KEY' : '81******************1d' 
}

#This is also another neccesary piece of information CMC needs. We are specifying that     we want the data in the form of JSON and giving a API key. An API Key is the "password" for the API, you can get this from the CMC sign up page

```

<aside>
🚨 **CAUTION: These dictionaries(parameters and headers) are absolutely essential and need to be typed perfectly for the API to recognize what you want**

</aside>

The final line( or two) that finally gives us the data in a way we can work take all the convenient information declared above and give us a JSON file

```python
session = Session() 
session.headers.update(headers) 

#We can use the session function(import session btw!) to store all of our information    into a, for a lack of a better word, **session**
```

## Where the fun begins

This is where we can start working with out data

```python
def ethPriceReport():
    response = session.get(url, params=parameters)  # gets the JSON file from the API
    data = json.loads(response.text)

    #Here we're using the convenient session to access the API data by passing in the 
    #url variable and parameters dictionary we defined earlier

   
```

This next block is where we sift through all the nested dictionaries for the information we actually want

```python
    ethPrice = data['data']['ETH'][0]['quote']['USD']['price']
    ethPercentChangeHourly = data['data']['ETH'][0]['quote']['USD']['percent_change_1h']
    ethPercentChangeDaily = data['data']['ETH'][0]['quote']['USD']['percent_change_24h']
    ethPercentChangeWeekly = data['data']['ETH'][0]['quote']['USD']['percent_change_7d']

    #Here we see sift through the multi layered dictionaries to access the elements 
    #we want

```

### Huh? why are there so many brackets?

The insane amount of brackets to access the elements aren’t doing any justice to a simple visualization to what they **actually mean**

- Data
    - ETH
        - quote
            - USD
                - price
                - percent_change_1h
                - percent_change_24h
                - percent_change_7d

Hopefully this dropdown explained the data structure we are going through to find the items we need. Head over to the [CMC documentation](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest) to get a more in-depth look at what the JSON file look likes

After we store those variables with the information we need, they need to be packaged up in a convenient format to be used later (Hint: It starts with a D and ends in a Y)

```python
priceReportETH = {
        'priceETH' : ethPrice,
        'percentChangeHRLY' : ethPercentChangeHourly,
        'percentChangeDAILY' : ethPercentChangeDaily,
        'percentChangeWEEKLY': ethPercentChangeWeekly,
    }
return priceReportETH
```

---
# How is the info being sent?
Sending Messages via Phone Number:

<aside>

💡 A significant part of this solution is credited to a [Alfredo Sequida's Tutorial](https://www.youtube.com/watch?v=4-ysecoraKo&ab_channel=AlfredoSequeida).

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
from tether.providers import PROVIDERS
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