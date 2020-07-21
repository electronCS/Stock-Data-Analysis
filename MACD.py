from collections import defaultdict
from Data import Data
from EMA26 import EMA26
from EMA12 import EMA12

class MACD:
    data = start = MACD = EMA12 = EMA26 = None;

    def __init__(self,data):
        self.data = data
        self.start = data.startDay()
        self.EMA12 = EMA12(data)
        self.EMA26 = EMA26(data)
        self.calcMACD()

    def calcMACD(self):
        self.MACD = defaultdict(lambda: 0)
        for x in range(self.start,self.data.getYesterday()+1):
            val = self.EMA12.get(x) - self.EMA26.get(x)
            self.MACD[x] = val
        # now = self.data.getToday()
        # val = self.EMA12.get(now) - self.EMA26.get(now)
        # self.MACD[now] = val

    def currentMACD():
        now = self.data.getToday()
        # val = self.EMA12.currentEMA12() - self.EMA26.currentEMA26()
        # self.MACD[now] = val
        # return val

    def get(self,day):
        if(self.MACD[day] == 0):
            raise Exception('does not have MACD value for ' + self.data.getDate(day))
        return self.MACD[day]

    def printMACD(self):
        for k,v in self.MACD.items():
            print(self.data.getDate(k), v)
