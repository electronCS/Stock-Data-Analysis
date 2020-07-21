class Simulator:
    today,yesterday,under,over,ticker,data
    EMA12 = EMA12()
    EMA26 = EMA26()
    MACD = MACD()
    
    def _init_(self, ticker):
        self.ticker = ticker
        today = '2020-07-16'
        yesterday = '2020-07-15'
        start = '2019-01-02'
        data = Data(ticker,today,yesterday,start)
        under = False
        over = False
        simulate()

    def simulate():
        print('STOCK --- ' + ticker)
        reg = regularTrade(data.startDay())
        print()
