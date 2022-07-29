from requests import Request, Session
import json
import time
import itertools


class EtherStream:
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

        self.parameters = {
            'symbol': 'ETH',
            'convert': 'USD'
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '81a0d3ef-430f-4b71-83e9-5b8ca264301d'
        }

        self.session = Session()
        self.session.headers.update(headers)

    def eth_price_report(self):
        """Returns a dictionary of useful information on Etherium currently

            Args:

            Returns:
                price_report_eth(dict) : A dictionary with information on Etherium currently(Price, percent change, etc.)
        """
        response = self.session.get(self.url, params=self.parameters)  # gets the JSON file from the API
        data = json.loads(response.text)

        eth_price = data['data']['ETH'][0]['quote']['USD']['price']
        eth_percent_change_hourly = data['data']['ETH'][0]['quote']['USD']['percent_change_1h']
        eth_percent_change_daily = data['data']['ETH'][0]['quote']['USD']['percent_change_24h']
        eth_percent_change_weekly = data['data']['ETH'][0]['quote']['USD']['percent_change_7d']

        price_report_eth = {
            'price_eth': eth_price,
            'percent_change_hourly': eth_percent_change_hourly,
            'percent_change_daily': eth_percent_change_daily,
            'percent_change_weekly': eth_percent_change_weekly,
        }

        return price_report_eth
