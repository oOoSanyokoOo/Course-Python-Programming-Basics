from math import sqrt
i = 0


def fail():
    global i
    n = int(input())
    if n == 0:
        return 0
    if sqrt(n) - int(sqrt(n)) == 0:
        i += 1
        fail()
        return print(n, end=' ')
    fail()


fail()
if i == 0:
    print(0)
