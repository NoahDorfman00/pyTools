from os import lchown
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import math

tkrStr = "MSFT"

tkr = yf.Ticker("MSFT")

# historical stock price
data = np.array(tkr.history(period='3mo'))

numPoints = np.shape(data)[0]
print(numPoints)

op = np.array(data[:,0])
hi = np.array(data[:,1])
lo = np.array(data[:,2])
cl = np.array(data[:,3])
time = np.arange(numPoints, dtype='float')
newTime = np.arange(numPoints, step=0.25)

y = np.zeros(np.shape(newTime)[0])
loTimes = np.array(time)
hiTimes = np.array(time)

for i in range(numPoints):
    y[i*4] = op[i]

    if abs(op[i] - lo[i]) < abs(op[i] - hi[i]):
        y[i*4 + 1] = lo[i]
        loTimes[i] = loTimes[i] + 0.25
        y[i*4 + 2] = hi[i]
        hiTimes[i] = hiTimes[i] + 0.5
    else:
        y[i*4 + 1] = hi[i]
        hiTimes[i] = hiTimes[i] + 0.25
        y[i*4 + 2] = lo[i]
        loTimes[i] = loTimes[i] + 0.5

    y[i*4 + 3] = cl[i]

avg = np.mean(y)
sumOfSqs = np.sum((y - avg)**2)
stdDev = math.sqrt(sumOfSqs / np.shape(y)[0])

#print(newTime, y)
#print(loTimes, lo)
#print(hiTimes, hi)
#plt.plot(time, hi, color='green')
#plt.plot(time, lo, color='red')
#plt.plot(time, op, color='black')
#plt.plot(time, cl, color='black')
plt.scatter(loTimes, lo, color='red')
plt.scatter(hiTimes, hi, color='green')
plt.plot(newTime, y, color='blue')
plt.axhline(avg, color='black')
plt.axhline(avg + stdDev, color='black', ls='--')
plt.axhline(avg - stdDev, color='black', ls='--')
plt.show()