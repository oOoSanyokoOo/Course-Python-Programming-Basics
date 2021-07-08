n = int(input())
m1 = n
m2 = 0
while n != 0:
    n = int(input())
    if m1 < n:
        m2 = m1
        m1 = n
    elif n != 0 and m2 < n:
        m2 = n
print(m2)
