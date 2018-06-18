from botlog import BotLog
from colorama import init
from poloniex import poloniex
init()



pair = "BTC_XMR"
orderNumber = ""
conn = poloniex('Key','Secret')
prices = []
#currentValues = conn.api_query("returnTicker")
#lastPairPrice = currentValues[pair]["last"]
#dataDate = datetime.datetime.now()



class BotTrade(object):
	def __init__(self,currentPrice,stopLoss=0):
		self.output = BotLog()
		self.status = "OPEN"
		self.entryPrice = currentPrice
		self.exitPrice = ""
		#orderNumber = conn.sell(pair, lastPairPrice, .01)
		#orderNumber = conn.buy(pair, lastPairPrice, .01)
		self.output.log("Trade opened")
		if (stopLoss):
			self.stopLoss = currentPrice - stopLoss
	
	def close(self,currentPrice):
		self.status = "CLOSED"
		self.exitPrice = currentPrice
		#conn.cancel (pair, orderNumber)
		self.output.log("Trade closed")
	def tick(self, currentPrice):
		if (self.stopLoss):
			if (currentPrice < self.stopLoss):
				self.close(currentPrice)


	def showTrade(self):
		tradeStatus = "Entry Price: "+str(self.entryPrice)+" Status: "+str(self.status)+" Exit Price: "+str(self.exitPrice)

		if (self.status == "CLOSED"):
			tradeStatus = tradeStatus + " Profit: "
			if (self.exitPrice > self.entryPrice):
				tradeStatus = tradeStatus + "\033[92m"
			else:
				tradeStatus = tradeStatus + "\033[91m"

			tradeStatus = tradeStatus+str(self.exitPrice - self.entryPrice)+"\033[0m"

		self.output.log(tradeStatus)
	