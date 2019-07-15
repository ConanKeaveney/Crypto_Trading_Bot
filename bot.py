import sys
import getopt
import time
import datetime
import pprint

from cryptotrading.src.Crypto_Trading_Bot_py3.botchart import BotChart
from cryptotrading.src.Crypto_Trading_Bot_py3.botstrategy import BotStrategy
from cryptotrading.src.Crypto_Trading_Bot_py3.botlog import BotLog
from cryptotrading.src.Crypto_Trading_Bot_py3.botcandlestick import BotCandlestick


def main(argv):

    startTime = True
    endTime = True

    try:
        opts, args = getopt.getopt(argv, "hp:c:n:s:e:", [
                                   "period=", "currency=", "points="])
    except getopt.GetoptError:
        print('trading-bot.py -p <period length> -c <currency pair> -n <period of moving average>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(
                'trading-bot.py -p <period length> -c <currency pair> -n <period of moving average>')
            sys.exit()
        elif opt in ("-p", "--period"):
            if (int(arg) in [300, 900, 1800, 7200, 14400, 86400]):
                period = arg
            else:
                print(
                    'Poloniex requires periods in 300,900,1800,7200,14400, or 86400 second increments')
                sys.exit(2)
        elif opt in ("-c", "--currency"):
            pair = arg
        elif opt in ("-n", "--points"):
            lengthOfMA = int(arg)
        elif opt in ("-s"):
            startTime = arg
            #startTime = datetime.datetime.now()
        elif opt in ("-e"):
            endTime = arg
            #endTime = startTime - datetime.timedelta(days=90)

    if (startTime):
        chart = BotChart("poloniex", "BTC_XMR", 300)

        strategy = BotStrategy()

        for candlestick in chart.getPoints():
            strategy.tick(candlestick)

    else:
        chart = BotChart("poloniex", "BTC_XMR", 300, False)

        strategy = BotStrategy()

        candlesticks = []
        developingCandlestick = BotCandlestick()

        while True:
            try:
                developingCandlestick.tick(chart.getCurrentPrice())
            except urllib2.URLError:
                time.sleep(int(30))
                developingCandlestick.tick(chart.getCurrentPrice())

            if (developingCandlestick.isClosed()):
                candlesticks.append(developingCandlestick)
                strategy.tick(developingCandlestick)
                developingCandlestick = BotCandlestick()

            time.sleep(int(30))

    endlog = strategy.showFinal()#list of trades

    for x in range(len(endlog)): 
        print(endlog[x])


if __name__ == "__main__":
    main(sys.argv[1:])
