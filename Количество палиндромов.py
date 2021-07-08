n = int(input())
i = 0
m = 1
while n >= m:
    a = str()
    k = 1
    while k <= m:
        a += str((m % (k * 10)) // k)
        k = k * 10
    if str(m) == a:
        i = i + 1
    m += 1
print(i)
