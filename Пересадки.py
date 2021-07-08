n = list(map(int, input().split()))
a, b = list([n[0], n[1]]), list([n[2], n[3]])
a.sort(), b.sort()
a1, a2 = set(), set()

for i in range(a[0], a[1] + 1):
    a1.add(i)
for j in range(b[0], b[1] + 1):
    a2.add(j)
print(len(a1 & a2))
