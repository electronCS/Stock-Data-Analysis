from collections import defaultdict
from Data import Data
from MACD import MACD

class MACDSignalLine:
    data = start = SignalLine = MACD = None;
    SMOOTHING = 2

    def __init__(self,data):
        self.data = data
        self.start = data.startDay()
        self.MACD = MACD(data)
        self.calcSignalLine()

    def calcSignalLine(self):
        self.SignalLine = defaultdict()
        SMA = 0
        for x in range(self.start,self.start+9):
            SMA += self.MACD.get(x)
        SMA = SMA/9
        self.SignalLine[self.start+8] = SMA
        k = self.SMOOTHING/float(9+1)
        for x in range(self.start+9,self.data.getYesterday()+1):
            val = self.MACD.get(x)*k + self.SignalLine[x-1]*(1-k)
            self.SignalLine[x] = val
        # now = self.data.getToday()
        # val = self.MACD.get(now)*k + self.SignalLine[now-1]*(1-k)
        # SignalLine[now] = val

    def currentSignalLine(self):
        now = self.data.getToday()
        # k = SMOOTHING/float(9+1)
        # val = self.MACD.get(now)*k + self.SignalLine[now-1]*(1-k)
        # SignalLine[now] = val
        # return val

    def get(self,day):
        return self.SignalLine[day]

    def printSignalLine(self):
        for k,v in self.SignalLine.items():
            print(self.data.getDate(k),v)
