from math import factorial
k = 0
n = int(input())
for i in range(1, n + 1):
    k = k + factorial(i)
print(k)
