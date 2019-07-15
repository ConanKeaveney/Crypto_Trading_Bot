from cryptotrading.src.Crypto_Trading_Bot_py3.botlog import BotLog
from cryptotrading.src.Crypto_Trading_Bot_py3.botindicators import BotIndicators
from cryptotrading.src.Crypto_Trading_Bot_py3.bottrade import BotTrade


class BotStrategy(object):
    def __init__(self):
        self.output = BotLog()
        self.prices = []
        self.closes = []  # Needed for Momentum Indicator
        self.trades = []
        self.currentPrice = ""
        self.currentClose = ""
        self.numSimulTrades = 1
        self.indicators = BotIndicators()
        

    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.prices.append(self.currentPrice)

        #self.currentClose = float(candlestick['close'])
        # self.closes.append(self.currentClose)

        self.output.log("Price: "+str(candlestick.priceAverage) +
                        "\tMoving Average: "+str(self.indicators.movingAverage(self.prices, 15)))

        self.evaluatePositions()
        self.updateOpenTrades()
        self.showPositions()

    def evaluatePositions(self):
        openTrades = []
        for trade in self.trades:
            if (trade.status == "OPEN"):
                openTrades.append(trade)

        if (len(openTrades) < self.numSimulTrades):
            if (self.currentPrice < self.indicators.movingAverage(self.prices, 20)):
                self.trades.append(
                    BotTrade(self.currentPrice, stopLoss=.00001))

        for trade in openTrades:
            if (self.currentPrice > self.indicators.movingAverage(self.prices, 20)):
                trade.close(self.currentPrice)

    def updateOpenTrades(self):
        for trade in self.trades:
            if (trade.status == "OPEN"):
                trade.tick(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
    
    def showFinal(self):
        return self.output.end()
