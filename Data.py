from collections import defaultdict

class Data:
    openP = close = high = low = dateToDay = volume = None;
    ticker = today = yesterday = start = dayToDate = None;

    def __init__(self,ticker,today,yesterday,start):
        self.openP = defaultdict(lambda: 0)
        self.close = defaultdict(lambda: 0)
        self.high = defaultdict(lambda: 0)
        self.low = defaultdict(lambda: 0)
        self.volume = defaultdict(lambda: 0)
        self.dateToDay = defaultdict(lambda: 0)
        self.dayToDate = defaultdict(lambda: "")
        self.ticker = ticker
        self.today = today
        self.yesterday = yesterday
        self.start = start
        self.pastData()

    def pastData(self):
        f = open(self.ticker + '.csv')
        data = []
        for x in f:
            data.append(x)
        for x in range(1,len(data)):
            vals = data[x].split(',')
            date = vals[0]
            self.openP[date] = float(vals[1])
            self.close[date] = float(vals[2])
            self.high[date] = float(vals[3])
            self.low[date] = float(vals[4])
            self.volume[date] = float(vals[5])
            self.dateToDay[date] = x
            self.dayToDate[x] = date
        self.dateToDay[self.today] = len(data)-1
        self.dayToDate[len(data)-1] = self.today
        f.close()

    def getDate(self,day):
        return self.dayToDate[day]

    def getToday(self):
        return self.dateToDay[self.today]

    def getYesterday(self):
        return self.dateToDay[self.yesterday]

    def getDay(self,date):
        return self.dateToDay[date]

    def startDay(self):
        return self.getDay(self.start)

    def closePrice(self,day):
        return self.close[self.getDate(day)]

    def highPrice(self,day):
        return self.high[self.getDate(day)]

    def lowPrice(self,day):
        return self.low[self.getDate(day)]

    def openPrice(self,day):
        return self.openP[self.getDate(day)]

    def volume(self,day):
        return self.volume[self.getDate(day)]

    def ticker():
        return self.ticker
