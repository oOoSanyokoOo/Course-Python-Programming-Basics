n = int(input())
imax = 1
imin = 1
a = n
counter = 1
while n != 0:
    if n == a:
        imin = 1
        imax = 1
    if n > a:
        imin = 1
        imax += 1
        a = n
        n = int(input())
        if counter < imax:
            counter = imax
    elif n < a:
        imax = 1
        imin += 1
        a = n
        n = int(input())
        if counter < imin:
            counter = imin
    else:
        n = int(input())
print(counter)
