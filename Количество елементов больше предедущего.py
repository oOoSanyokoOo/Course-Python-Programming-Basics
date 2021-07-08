n = int(input())
a = 0
p = n
while n != 0:
    a += (n > p)
    p = n
    n = int(input())
print(a)
