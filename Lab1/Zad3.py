from numpy import float32

def dzeta32(s, n, is_forward):
    result = float32(0)

    if is_forward == True:

        for k in range(1, n+1):
            result += float32(k ** -s)

    else:
        for k in range(n, 0, -1):
            result += float32(k ** -s)

    return result

def eta32(s, n, is_forward):
    result = float32(0)

    if is_forward == True:
        for k in range(1, n+1):
            if k % 2 == 0:
                result -= float32(k ** -s)
            else:
                result += float32(k ** -s)
    else:
        for k in range(n, 0, -1):
            if k % 2 == 0:
                result -= float32(k ** -s)
            else:
                result += float32(k ** -s)

    return result

def dzeta64(s, n, is_forward):
    result = 0

    if is_forward == True:

        for k in range(1, n+1):
            result += k ** -s

    else:
        for k in range(n, 0, -1):
            result += k ** -s

    return result

def eta64(s, n, is_forward):
    result = 0

    if is_forward == True:
        for k in range(1, n+1):
            if k % 2 == 0:
                result -= float32(k ** -s)
            else:
                result += float32(k ** -s)
    else:
        for k in range(n, 0, -1):
            if k % 2 == 0:
                result -= k ** -s
            else:
                result += k ** -s

    return result

n_list = [50, 100, 200, 500, 1000]
s_list = [2, 3.6667, 5, 7.2, 10]

print("single precision: ")
print("dzeta function: ")
print("s     forward      backwards     diff")
for n in n_list:
    print("n = ", n)
    for s in s_list:
        backwards = dzeta32(s, n, False)
        forward = dzeta32(s, n, True)
        print(s, ":", forward, ":", backwards, ":", forward - backwards)

print("eta function: ")
print("s     forward      backwards     diff")
for n in n_list:
    print("n = ", n)
    for s in s_list:
        backwards = eta32(s, n, False)
        forward = eta32(s, n, True)
        print(s, ":", forward, ":", backwards, ":", forward - backwards)

print("double precision: ")
print("dzeta function: ")
print("s     forward      backwards     diff")
for n in n_list:
    print("n = ", n)
    for s in s_list:
        backwards = dzeta64(s, n, False)
        forward = dzeta64(s, n, True)
        print(s, ":", forward, ":", backwards, ":", forward - backwards)

print("eta function: ")
print("s     forward      backwards     diff")
for n in n_list:
    print("n = ", n)
    for s in s_list:
        backwards = eta64(s, n, False)
        forward = eta64(s, n, True)
        print(s, ":", forward, ":", backwards, ":", forward - backwards)



# widać, że wartość backwards ma często większą wartość niż forwad
# czyli najprawdopodobniej jest ona wyliczana w dokładniejszy sposób
# zgadza się to z teoretycznymi przewidywaniami, ponieważ wyliczane kolejne
# wartości są coraz mniejsze, czyli sumując od tyłu cały czas będę
# operował na wartościach o podobnym rzędzie wielkości co zminimalizuje niedokładość
# reprezentacji zmiennoprzecinkowej

#



