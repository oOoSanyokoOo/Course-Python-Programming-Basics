from math import sqrt
x1 = int(input())
li = []
if x1 == 0:
    li.append(0)
elif x1 < 4:
    li.append(1)


def fail(x, b, f2):
    global li
    while x > 1:
        if sqrt(x) % 1 == 0:
            if f2 > 0:
                x = f2**2-1
                f2 = 0
            else:
                li.append(int(sqrt(x)))
                break
        else:
            x -= 1
    x = b - x
    b = x
    if x > 3:
        fail(x, b, f2)
    elif x > 0:
        while x > 0:
            li.append(1)
            x -= 1
        if len(li) > 4:
            lg = li[0]
            li = []
            fail(x1, x1, lg)
    else:
        if len(li) > 4:
            lg = li[0]
            li = []
            fail(x1, x1, lg)


fail(x1, x1, 0)

for i in li:
    print(i, end=' ')
