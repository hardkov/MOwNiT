from matplotlib import pyplot as plt
from numpy import float32
import time

val64 = 0.53125
val32 = float32(0.53125)
sum32 = float32(0)
sum64 = 0
tmpError = 0

numbersToSum = [val32] * 10 ** 7
errList = []

startTime = time.time()

for i in range(10**7):
    sum32 += numbersToSum[i]
    if i % 25000 == 0:
        sum64 = val64 * (i+1)
        tmpError = sum64 - sum32
        errList.append(tmpError/sum64)

print(time.time() - startTime)
plt.plot(errList)
plt.show()

#czas wykonania: 3.7322134971618652 bez zliczania err

