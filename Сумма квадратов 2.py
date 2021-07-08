from math import *


def fail(n, a, k):
    c = n
    d = k
    while c > 0:
        if d > 0:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3))))) - 1
            d -= 1
        else:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3)))))
        if x <= 1:
            x = trunc(float('{0:.11f}'.format((c ** (1 / 3)))))
        if d > x:
            print(0)
            exit(0)
        a.append(x ** 3)
        c -= x ** 3
        if len(a) > 7:
            a.clear()
            fail(n, a, k + 1)
    print(*a)
    exit(0)


a = []
n = int(input())
k = 0
fail(n, a, k)
