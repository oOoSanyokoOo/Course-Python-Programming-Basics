n = list(map(int, input().split()))
for i in range(len(n) // 2):
    n[i], n[len(n) - 1 - i] = n[len(n) - 1 - i], n[i]
print(*n)
