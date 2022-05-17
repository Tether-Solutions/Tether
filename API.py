from requests import Request, Session
import json
import time
import itertools

import sendMessages as SMS

numberList = ["8045479964", "8042456976"]

#HELLO

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest' #URL of the data api

parameters = {
    'symbol' : 'ETH', #Specifies what currency we want
    'convert' : 'USD' #Converts the specified currency into something we want
}

headers = {
    'Accepts' : 'application/json', #specifying that we want data in JSON format
    'X-CMC_PRO_API_KEY' : '81a0d3ef-430f-4b71-83e9-5b8ca264301d' #the key the coinmarketcap gives to acces date; essentially a password
}

delayBetweenRequests = 60
percentageThreshold = 0.02

session = Session() #saves information like cookies and saves time
session.headers.update(headers) #passess in the required information to the api


def ethPriceReport():
    response = session.get(url, params=parameters)  # gets the JSON file from the API
    data = json.loads(response.text)

    ethPrice = data['data']['ETH'][0]['quote']['USD']['price']

    ethPercentChangeHourly = data['data']['ETH'][0]['quote']['USD']['percent_change_1h']
    ethPercentChangeDaily = data['data']['ETH'][0]['quote']['USD']['percent_change_24h']
    ethPercentChangeWeekly = data['data']['ETH'][0]['quote']['USD']['percent_change_7d']

    priceReportETH = {
        'priceETH' : ethPrice,
        'percentChangeHRLY' : ethPercentChangeHourly,
        'percentChangeDAILY' : ethPercentChangeDaily,
        'percentChangeWEEKLY': ethPercentChangeWeekly,
    }
    return priceReportETH


for x in itertools.repeat([]): #Infinite Loop
    if (ethPriceReport()['percentChangeHRLY'] > percentageThreshold):
      for number in numberList: #iterates through numberList sending the message to each number 
        SMS.priceReportUP(ethPriceReport()['percentChangeHRLY'], ethPriceReport()['priceETH'], number)
        print("Sent Price Report UP")
        
    if (ethPriceReport()['percentChangeHRLY'] < -percentageThreshold):
      for number in numberList:
        SMS.priceReportDOWN(ethPriceReport()['percentChangeHRLY'], ethPriceReport()['priceETH'], number)
        print("Sent Price Report Down")
    time.sleep(delayBetweenRequests)  # delay between requests
