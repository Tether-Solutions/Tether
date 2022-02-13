from requests import Request, Session
import json
import pprint


url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest' #URL of the data api

parameters = {
    'symbol' : 'ETH', #Specifies what currency we want
    'convert' : 'USD' #Converts the specified currency into something we want
}

headers = {
    'Accepts' : 'application/json', #specifying that we want data in JSON format
    'X-CMC_PRO_API_KEY' : '81a0d3ef-430f-4b71-83e9-5b8ca264301d' #the key the coinmarketcap gives to acces date; essentially a password
}

session = Session() #saves information like cookies and saves time
session.headers.update(headers) #passess in the required information to the api

response = session.get(url, params=parameters) #gets the JSON file from the API
data = json.loads(response.text)

ethPrice = data['data']['ETH'][0]['quote']['USD']['price']

print("Etherium Price for Today: " + ethPrice)

