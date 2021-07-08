n, x = int(input()), float(input())
s = 0
while n >= 0:
    a = float(input())
    i = 0
    xs = 1
    while i < n:
        xs *= x
        i += 1
    sm = a * xs
    n -= 1
    s += sm
print(s)
