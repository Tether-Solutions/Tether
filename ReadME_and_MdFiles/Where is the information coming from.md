# Where is the information coming from?

Yuvanesh Anand

Getting Started on sending ETH Reports to Your Phone

# What needs to be done?

There are a couple steps needed to get ETH(and hopefully other currency) reports sent to your phone. We need to pull the information from C[oinMarketCap](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical)’s API, and package that information in a sensible, easy to read package over text. 

# Where is the info coming from?

## The Setup

We use [API.py](http://API.py) to access information from CoinMarketCap’s database

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