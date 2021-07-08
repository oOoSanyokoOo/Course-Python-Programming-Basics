import math
x = int(input())
q = 0
a = 0
n = 0
while x != 0:
    q += x**2
    a += x
    n += 1
    x = int(input())
print(math.sqrt((q - a**2 / n) / (n - 1)))
