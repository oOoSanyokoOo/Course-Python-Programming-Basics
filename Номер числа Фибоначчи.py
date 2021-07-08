n = int(input())
a = 0
b = 1
i = 0
while a < n:
    b, a = a + b, b
    i += 1
if a == n:
    print(i)
else:
    print(-1)
