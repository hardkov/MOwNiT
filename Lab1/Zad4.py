from numpy import float32
from matplotlib import pyplot as plt
import numpy as np


def projection64(r_min, r_max,  x):
    P = np.linspace(r_min, r_max, 10000)
    X = []
    Y = []
    for r in P:
        X.append(r)
        for i in range(1000):
            x = (r * x) * (1 - x)

        Y.append(x)

    plt.plot(X, Y, marker=',', ls='')
    plt.show()

def trajectory64(x, r):
    Y = []

    for i in range(100000):
        Y.append(x)
        x = (r * x) * (1 - x)

    plt.plot(Y, marker=',', ls='')
    plt.show()

def trajectory32(x, r):
    Y = []

    for i in range(100000):
        Y.append(float32(x))
        x = float32((r * x) * (1 - x))

    plt.plot(Y, marker=',', ls='')
    plt.show()


def limit64(x, r):
    i = 0
    while x != 0:
        x = (r * x) * (1 - x)
        i += 1
    return i


def limit32(x, r):
    i = 0
    while x != 0:
        x = float32((r * x) * (1 - x))
        i += 1
    return i


trajectory32(float32(0.53125), float32(3.77))
trajectory64(0.53125, 3.77)

# dla 10000 różnych wartości r z przedzialu <1,4> oraz
# kilku wartości x0: 0.5, 0.53125, 0.999, 0.1234. 0.3
# wygenerowałem diagram bifurakcyjny i wyglądają one tak samo.
# wnioskuje z tego, że postać diagramu nie jest zależna od wartosci poczatkowej x0

# dla różnych x0 wszystkie wartości zbiegają do wartości zależnej od parametru r
# do r = 3 iteracje zmierzają do liczby o prostej zależności od parametru r
# od r = 3 sprawa się komplikuje i zaczyna panować chaos.
# z tego wynika, że w r = 3 występuje zjawisko bifurakcji
# niewielka zmiana parametru r powoduje diametralną zmianę punktu zbieżności

# dla wartości r z przedziału <3.75, 3.8>
# wykresy trajektori iteracji dla pojedynczej precyzji oraz podwójnej różnią się tym,
# że dla 64bit widać niewystępujące wartości jako gęsto ustawione kropki, a w 32bit
# są to ciągłe linie. Lepsza precyzja pozwala przedstawić niewidoczne w pojedyńczej prezycji
# miejsca. Generalizując, dla różnych rozmiarów pętli, puste miejsca na wykresie są
# bardziej skupione oraz ustrukturyzowane, czyli nasz model staje się coraz mniej chaotyczny.
# Wynika to najprawdopodobniej z tego, że dokonując kolejnych obliczeń w 64bit precyzji komplikujemy
# wszystko a w 32bit wartości te są gubione i nie zmieniają sie.

# numer iteracji po której dla pojedynczej oraz podwójnej precyzji x osiąga zero:
#             32bit         64bit
# 0.5         2             2
# 0.53125     3362          ?
# 0.999       796           ?
# 0.1234      2441          ?
# 0.3         1100          ?

# dla pojedynczej precyzji zero jest osiągane po kilku tysiącach iteracji











