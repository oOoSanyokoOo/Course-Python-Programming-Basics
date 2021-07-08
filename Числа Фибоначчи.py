n = int(input())
a, b, i = 0, 1, 1
s = a + b
while i != n:
    s = a + b
    a = b
    b = s
    i += 1
print(s)
