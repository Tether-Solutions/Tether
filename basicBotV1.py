import time
import itertools
from API import ethPriceReport
import csv

ethPrice = ethPriceReport()['priceETH']
seconds = time.time()



def logger(sec, eth, usd, percentChange):
    with open('priceDataCsv.csv', 'w', newline='') as f:
        fieldnames = ['time', 'ethReserve', 'usdReserve']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        currentTime = time.ctime(sec)

        thewriter.writeheader()
        thewriter.writerow({'time' : currentTime,'ethReserve' : eth, 'usdReserve' : usd)

def reader():
    with open('priceDataCsv.csv', 'r') as f:
        reader = csv.DictReader(f)

        allLines = list(reader)
        latestLine = allLines[-1]

        ethReserves = latestLine['ethReserve']
        usdReserves = latestLine['usdReserve']

        returnDictionary = {
            'ethRes' : ethReserves,
            'usdRes' : usdReserves
        }

        return returnDictionary










def liquidate(seconds):
    simulationETH = reader()['ethRes']
    simulationUSD = reader()['usdRes']

    simulationETH -= amountToConvert
    simulationUSD += (amountToConvert * ethPrice)

    time.time()
    secs = time.ctime(seconds)
    logger(secs, simulationETH, simulationUSD)


def buyDip():
    simulationETH = reader()['ethRes']
    simulationUSD = reader()['usdRes']

    simulationETH += amountToConvert
    simulationUSD -= (amountToConvert * ethPrice)

    time.time()
    secs = time.ctime(seconds)
    logger(seconds, simulationETH, simulationUSD)



print("Check Check")
'''
for x in itertools.repeat([]):
    if (ethPriceReport()['percentChangeHRLY'] > 0.2):

        seconds = time.time()
    elif (ethPriceReport()['percentChangeHRLY'] < -0.2):

        seconds = time.time()
    time.sleep(120)
'''