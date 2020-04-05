from numpy import float32
import time

val64 = 0.999999
val32 = float32(0.999999)
numbersToSum = [val32] * 10 ** 7
sum32 = float32(0)
sum64 = 0

valMin32 = float32(0.00001)
valMax32 = float32(84.956)

valMin64 = 0.00001
valMax64 = 84.956

for i in range(10 ** 7):
    if i % 2 == 0:
        numbersToSum[i] = valMin32
    else:
        numbersToSum[i] = valMax32

startTime = time.time()


def listSum(list):
    iterationEnd = len(list)

    if iterationEnd == 1:
        return list[0]

    if iterationEnd == 0:
        return 0

    newList = []

    if iterationEnd % 2 == 1:
        newList.append(list[iterationEnd-1])
        iterationEnd -= 1

    for i in range(0, iterationEnd, 2):
        newList.append(list[i] + list[i+1])

    return listSum(newList)

sum32 = listSum(numbersToSum)
print(time.time() - startTime)
sum64 = 5 * (10 ** 6) * (valMax64 + valMin64)
print(sum64 - sum32)


# Błąd wyniosi 0.
# dzieje się tak, ponieważ sumując coraz większe liczby zamiast cały czas małych nie wychodzimy
# poza zasięg precyzji(wynik do którego dążymy jest 0 a więc mieści się na 32 bitach)
# czas wykonania: 4.3552491664886475
# nie zerowa wartość dla tablicy wypełnionej naprzemiennie wartościami 0.00001 oraz 84.956
# wynika to z tego, że dla sumy tych liczb wymagana jest duża precyzja (są zarówno liczby przed jak i po przecinkiem)



