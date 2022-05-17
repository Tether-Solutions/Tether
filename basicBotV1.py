import time
import itertools
from API import ethPriceReport
import csv
import pandas as pd
import os

ethPrice = ethPriceReport()['priceETH']
seconds = time.time()



def logger(sec, eth, usd):
    with open('priceData.csv', 'a', newline='\n') as f:
        fieldnames = ['time', 'ethReserve', 'usdReserve']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)



        #thewriter.writeheader()
        thewriter.writerow({'time' : sec,'ethReserve' : eth, 'usdReserve' : usd})

def reader():
    #df = pd.read_csv('priceData.csv', header=0)

    #print(df)

    with open('priceData.csv', 'r') as f:
        reader = csv.DictReader(f)

        
        allLines = list(reader)
        #print(allLines)
        latestLine = allLines[-1]

        ethReserves = latestLine['ethReserve']
        usdReserves = latestLine['usdReserve']

        returnDictionary = {
            'ethRes' : ethReserves,
            'usdRes' : usdReserves
        }

    return returnDictionary

def transactionMaker(transactionType, cryptoUsdPair):
    if(transactionType == 1):
        print("Buy Order Initiated")

        simulationETH = reader()['ethRes']
        simulationUSD = reader()['usdRes']

        simulationUSD = float(simulationUSD)
        simulationETH = float(simulationETH)

        # print(simulationETH) Test Prints
        # print(simulationUSD)
        # print(type(cryptoUsdPair))

        if(simulationUSD >= (0.25 * cryptoUsdPair)):
            simulationUSD -= (0.25 * cryptoUsdPair)
            simulationETH += 0.25

            logger(seconds, simulationETH, round(simulationUSD, 3))
        else:
            print("There were not enough funds(USD) to make the transaction")

    elif(transactionType == 2):
        print("Sell Order Initiated")

        simulationETH = reader()['ethRes']
        simulationUSD = reader()['usdRes']

        simulationUSD = float(simulationUSD)
        simulationETH = float(simulationETH)

        # print(simulationETH) Testing Prints
        # print(simulationUSD)
        # print(cryptoUsdPair)

        if(simulationETH >= 0.25):
            simulationUSD += (0.25 * cryptoUsdPair)
            simulationETH -= 0.25

            logger(seconds, simulationETH, round(simulationUSD, 3))
        else:
            print("There were not enough funds(ETH) to make the transcation")

def interface():
    print("Starting bot script")
    startUpInput = input("Would you like to start the automation process (Y / N)").lower()

    if (startUpInput in ['y', 'yes']):
        thresholdInput = int(input("What is the percentage threshold for making purchases(enter integers, e.x 1, 2, -1, -2 ... ) "))