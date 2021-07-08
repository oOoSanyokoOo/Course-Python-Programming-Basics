b = int(input())
n = list(map(int, input().split()))
a = int(input())
c = []
for i in range(b):
    c.append(abs(n[i] - a))
print(n[c.index(min(c))])
