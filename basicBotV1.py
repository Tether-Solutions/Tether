import time
import itertools
from API import ethPriceReport
import csv
import pandas as pd

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
        print(allLines)
        latestLine = allLines[-1]

        ethReserves = latestLine['ethReserve']
        usdReserves = latestLine['usdReserve']

        returnDictionary = {
            'ethRes' : ethReserves,
            'usdRes' : usdReserves
        }

        return returnDictionary




def liquidate(seconds, amountToConvert):
    currentPrice = float(reader()['ethRes'])
    if (currentPrice > 0.25):
        simulationETH = float(reader()['ethRes'])
        simulationUSD = float(reader()['usdRes'])

        simulationETH -= amountToConvert
        simulationUSD += (amountToConvert * ethPrice)

        time.time()
        secs = time.ctime(seconds)
        logger(secs, simulationETH, simulationUSD)


def buyDip(seconds, amountToConvert):
    simulationETH = float(reader()['ethRes'])
    simulationUSD = float(reader()['usdRes'])

    simulationETH += amountToConvert
    simulationUSD -= (amountToConvert * ethPrice)

    time.time()
    secs = time.ctime(seconds)
    logger(seconds, simulationETH, simulationUSD)





for x in itertools.repeat([]):
    if (ethPriceReport()['percentChangeHRLY'] > 0.02):
        seconds = time.time()
        liquidate(seconds, 0.25)
        print("Liquidated!")
    elif (ethPriceReport()['percentChangeHRLY'] < -0.02):
        seconds = time.time()
        buyDip(seconds, 0.25)
        print("bought dip")
    else:
        print("No trades happened in the last 2 minutes")
        print(ethPriceReport()['percentChangeHRLY'])
    time.sleep(120)
