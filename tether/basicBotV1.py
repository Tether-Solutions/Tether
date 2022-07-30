from datetime import datetime
import itertools
from report import EtherStream
import csv
# import pandas as pd
import os


class AutoBot:
    def __init__(self):
        self.ether_data = EtherStream()
        self.ether_price = self.ether_data.eth_price_report()['price_eth']
        self.ether_percent_change_hourly = self.ether_data.eth_price_report()['percent_change_hourly']

    def transaction(self, threshold: int):
        """
        1. Read what the current state of the account is
        2. Make the purchase
            a. If there is not enough funds, lower the purchase until purchase can be made( if it has to has to be reduced twice stop the purchase)
        3. Sell
        """
        if 0 > -1:
            with open('tether/data/price_data.csv', 'r') as f:
                last_line = f.readlines()[-1]

                print(type(last_line))
            pass
        elif self.ether_percent_change_hourly < -threshold:
            #Buy
            pass


if __name__ == "__main__":
    bot = AutoBot()

    bot.transaction(1)
