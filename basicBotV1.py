import time

simulationETH = 1
simulationUSD = 0

amountToConvert = 0.25

seconds = time.time()

def liquidate(ethPrice):
    simulationETH -= amountToConvert
    simulationUSD += amountToConvert * ethPrice
    print("Currently(" + time.ctime(seconds) + "), ETH reserves are at " + simulationETH + " and USDC reserves are at " + simulationUSD)

def buyDip(ethPrice):
    simulationETH += amountToConvert
    simulationUSD -= (amountToConvert * ethPrice)
    print("Currently(" + time.ctime(seconds) + "), ETH reserves are at " + simulationETH + " and USDC reserves are at " + simulationUSD)
