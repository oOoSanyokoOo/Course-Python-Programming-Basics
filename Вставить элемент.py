n = list(map(int, input().split()))
k, c = map(int, input().split())
n.append(c)
for i in range(len(n) - 1, k, -1):
    n[i], n[i - 1] = n[i - 1], n[i]
print(*n)
