from cryptotrading.src.Crypto_Trading_Bot_py3.botlog import BotLog


class BotTrade(object):
    total_prof = 0

    def __init__(self, currentPrice, stopLoss=0):
        self.output = BotLog()
        self.status = "OPEN"
        self.entryPrice = currentPrice
        self.exitPrice = ""
        self.output.log("Trade opened")
        if (stopLoss):
            self.stopLoss = currentPrice - stopLoss

    def close(self, currentPrice):
        self.status = "CLOSED"
        self.exitPrice = currentPrice
        self.output.log("Trade closed")

    def tick(self, currentPrice):
        if (self.stopLoss):
            if (currentPrice < self.stopLoss):
                self.close(currentPrice)

    def showTrade(self):
        tradeStatus = "Entry Price: " + \
            str(self.entryPrice)+" Status: "+str(self.status) + \
            " Exit Price: "+str(self.exitPrice)

        tradeStatus2 = "Entry Price: " + \
            str(self.entryPrice)+" Status: "+str(self.status) + \
            " Exit Price: "+str(self.exitPrice)

        if (self.status == "CLOSED"):
            tradeStatus = tradeStatus + " Profit: "
            tradeStatus2 = tradeStatus2 + " Profit: "

            if (self.exitPrice > self.entryPrice):
                tradeStatus = tradeStatus + "\033[92m"
            else:
                tradeStatus = tradeStatus + "\033[91m"

            tradeStatus = tradeStatus + \
                str(self.exitPrice - self.entryPrice)+"\033[0m"

            tradeStatus2 = tradeStatus2 + \
                str(self.exitPrice - self.entryPrice)

            BotTrade.total_prof += (self.exitPrice - self.entryPrice)
            tradeStatus = tradeStatus + " Total Profit: "
            tradeStatus2 = tradeStatus2 + " Total Profit: "
            if (BotTrade.total_prof > 0):
                tradeStatus = tradeStatus + "\033[92m"
            else:
                tradeStatus = tradeStatus + "\033[91m"

            tradeStatus = tradeStatus + \
                str(BotTrade.total_prof)+"\033[0m"
            tradeStatus2 = tradeStatus2 + \
                str(BotTrade.total_prof)

            self.output.tlog(tradeStatus2)

        self.output.log(tradeStatus)
