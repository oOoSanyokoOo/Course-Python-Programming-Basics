from math import floor, ceil

n = float(input())
if n * 10 % 10 < 5:
    print(floor(n))
else:
    print(ceil(n))
