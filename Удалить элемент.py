n = list(map(int, input().split()))
k = int(input())
for i in range(k + 1, len(n)):
    n[i - 1] = n[i]
n.pop()
print(*n)
