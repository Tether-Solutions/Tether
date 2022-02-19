import time
import itertools
from API import ethPriceReport

print("Check Check")

simulationETH = 1
simulationUSD = 1000
amountToConvert = 0.25
ethPrice = ethPriceReport()['priceETH']

seconds = time.time()

def liquidate():
    simulationETH -= amountToConvert
    simulationUSD += amountToConvert * ethPrice
    print("Currently(" + time.ctime(seconds) + "), ETH reserves are at " + str(simulationETH) + " and USDC reserves are at " + str(simulationUSD))



def buyDip():
    simulationETH += amountToConvert
    simulationUSD -= (amountToConvert * ethPrice)
    print("Currently(" + time.ctime(seconds) + "), ETH reserves are at " + str(simulationETH) + " and USDC reserves are at " + str(simulationUSD))

print("Check Check")

for x in itertools.repeat([]):
    if (ethPriceReport()['percentChangeHRLY'] > 0.02):
        liquidate()
    elif (ethPriceReport()['percentChangeHRLY'] < 0.02):
        buyDip()