import sys, getopt

from botchart import BotChart
from botstrategy import BotStrategy

def main(argv):
	#change chart depending on exchange and Crypto Currency
	#chart = BotChart("poloniex","BTC-WAVES",300)

	strategy = BotStrategy()

	#for candlestick in chart.getPoints():
		#strategy.tick(candlestick)

if __name__ == "__main__":
	main(sys.argv[1:])
