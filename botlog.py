class BotLog(object):
	tradelog = []

	def __init__(self):
		pass

	def log(self, message):
		pass
		#print(message)

	def tlog(self, message):
		spl = message.split(' ')
		BotLog.tradelog.append([spl[2],spl[7],spl[9],spl[12]])
		#print("appended")


	def end(self):
		#print(BotLog.tradelog)
		return BotLog.tradelog