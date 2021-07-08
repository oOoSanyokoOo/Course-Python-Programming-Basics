n = int(input())
m = n
a = 0
while n != 0:
    if n > m:
        m = n
        a = 0
    if n == m:
        a += 1
    n = int(input())
print(a)
