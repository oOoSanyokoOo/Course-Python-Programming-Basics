n = int(input())
s = set()
k = set()
m = set()
for j in range(int(input())):
    m.add(str(input()))
k |= m
s |= m
for i in range(1, n):
    m = set()
    for j in range(int(input())):
        m.add(str(input()))
    k &= m
    s |= m
print(len(k))
for i in k:
    print(i)
print(len(s))
for i in s:
    print(i)
