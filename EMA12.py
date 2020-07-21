from collections import defaultdict
from Data import Data

class EMA12:
    start = data = EMA12 = None;
    SMOOTHING = 2;

    def __init__(self,data):
        self.data = data;
        self.start = data.startDay();
        self.EMA12 = defaultdict(lambda: 0);
        self.calcEMA12();

    def calcEMA12(self):
        SMA = 0;
        for i in range(self.start-11,self.start+1):
            SMA += self.data.closePrice(i);
        SMA = abs(SMA/12)
        self.EMA12[self.start] = SMA;
        k = self.SMOOTHING/float(12+1)
        for i in range(self.start+1,self.data.getYesterday()+1):
            val = self.data.closePrice(i)*k + self.EMA12[i-1]*(1-k)
            self.EMA12[i] = val
        # now = self.data.getToday()
        # val = Price.currentPrice(data.ticker())*k + EMA12[now-1]*(1-k)
        # EMA12[now] = val

    def currentEMA12():
        now = self.data.getToday()
        k = self.SMOOTHING/(12+1)
        # val = Price.currentPrice(data.ticker())*k + EMA12[now-1]*(1-k)
        # EMA12[now] = val
        # return val

    def get(self,day):
        if self.EMA12[day] == 0:
            raise Exception('does not have EMA12 value for ' + self.data.getDate(day))
        return self.EMA12[day]

    def printEMA12(self):
        for k,v in self.EMA12.items():
            print(self.data.getDate(k), v)
