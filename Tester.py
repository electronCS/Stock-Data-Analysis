from Data import Data
from MACD import MACD
from MACDSignalLine import MACDSignalLine

import matplotlib.pyplot as plt
from matplotlib import style


ticker = 'MDB'
today = '2020-07-17'
yesterday = '2020-07-16'
start = '2018-01-19'
data = Data(ticker,today,yesterday,start)
#print(len(data))
macd = MACD(data)
signal = MACDSignalLine(data)

values = []
for key in sorted(data.openP.keys()):
    values.append(data.openP.get(key))

x_axis = range(0, len(values))
plt.plot(x_axis, values)
#print(macd.MACD)
plt.plot(macd.MACD.keys(), macd.MACD.values())
plt.plot(signal.SignalLine.keys(), signal.SignalLine.values())

plt.show()
print(data.openP)
#signal.printSignalLine()
# macd.printMACD()
