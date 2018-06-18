from poloniex import poloniex
import urllib, json
import pprint
from botcandlestick import BotCandlestick

class BotChart(object):
	def __init__(self, exchange, pair, period, backtest=True):
		self.pair = pair
		self.period = period

		self.startTime = 1491048000
		self.endTime = 1491591200

		self.data = []
		
		if (exchange == "poloniex"):
			self.conn = poloniex('ZPJCGM29-U7HP3Z8Z-EXQYF4GE-W9SBKULA','71396818501f4b3434e53ecb33ee85f5f0e5da2d7a2f375b8b9aa3df43bef92897a3f5eaac7584f1352a6a799f048df9f62e97b953fce0a12d5fbe6cd657d1ab')

			if backtest:
				poloData = self.conn.api_query("returnChartData",{"currencyPair":self.pair,"start":self.startTime,"end":self.endTime,"period":self.period})
				for datum in poloData:
					if (datum['open'] and datum['close'] and datum['high'] and datum['low']):
						self.data.append(BotCandlestick(self.period,datum['open'],datum['close'],datum['high'],datum['low'],datum['weightedAverage']))

		if (exchange == "bittrex"):
			if backtest:
				url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName="+self.pair+"&tickInterval="+self.period+"&_="+str(self.startTime)
				response = urllib.urlopen(url)
				rawdata = json.loads(response.read())

				self.data = rawdata["result"]


	def getPoints(self):
		return self.data

	def getCurrentPrice(self):
		currentValues = self.conn.api_query("returnTicker")
		lastPairPrice = {}
		lastPairPrice = currentValues[self.pair]["last"]
		return lastPairPrice
