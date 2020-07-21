from collections import defaultdict
from Data import Data

class EMA26:
    start = data = EMA26 = None;
    SMOOTHING = 2;

    def __init__(self,data):
        self.data = data;
        self.start = data.startDay();
        self.EMA26 = defaultdict(lambda: 0);
        self.calcEMA26();

    def calcEMA26(self):
        SMA = 0;
        for i in range(self.start-25,self.start+1):
            SMA += self.data.closePrice(i);
        SMA = abs(SMA/26)
        self.EMA26[self.start] = SMA;
        k = float(self.SMOOTHING/float(26+1))
        for i in range(self.start+1,self.data.getYesterday()+1):
            val = self.data.closePrice(i)*k + self.EMA26[i-1]*(1.0-k)
            self.EMA26[i] = val
        # now = self.data.getToday()
        # val = Price.currentPrice(data.ticker())*k + EMA26[now-1]*(1-k)
        # EMA26[now] = val

    def currentEMA26():
        now = self.data.getToday()
        k = self.SMOOTHING/(26+1)
        # val = Price.currentPrice(data.ticker())*k + EMA26[now-1]*(1-k)
        # EMA26[now] = val
        # return val

    def get(self,day):
        if self.EMA26[day] == 0:
            raise Exception('does not have EMA26 value for ' + self.data.getDate(day))
        return self.EMA26[day]

    def printEMA26(self):
        for k,v in self.EMA26.items():
            print(self.data.getDate(k), v)
