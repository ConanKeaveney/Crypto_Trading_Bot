import sys
import getopt
import time
import datetime
import pprint

from cryptotrading.src.Crypto_Trading_Bot_py3.botchart import BotChart
from cryptotrading.src.Crypto_Trading_Bot_py3.botstrategy import BotStrategy
from cryptotrading.src.Crypto_Trading_Bot_py3.botlog import BotLog
from cryptotrading.src.Crypto_Trading_Bot_py3.botcandlestick import BotCandlestick

class TradeLog(object):
    def Generate(self):
        startTime = True
        endTime = True


        if (startTime):
            chart = BotChart("poloniex", "BTC_XMR", 300)

            strategy = BotStrategy()

            for candlestick in chart.getPoints():
                strategy.tick(candlestick)

        


        endlog = strategy.showFinal()#list of trades
        

            # for x in range(len(endlog)): 
            #     print(endlog[x])

        return endlog