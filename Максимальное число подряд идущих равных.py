n = int(input())
c = max = 1
while n != 0:
    a = n
    n = int(input())
    if n == a:
        c += 1
        if max <= c:
            max = c
    else:
        c = 1
print(max)
