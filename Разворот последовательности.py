def raz():
    n = int(input())
    if n == 0:
        return print(n)
    raz()
    return print(n)


raz()
