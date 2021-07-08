n = float(input())
a = 0
b = 1
while b <= n:
    a += (1 / (b ** 2))
    b += 1
print(a)
