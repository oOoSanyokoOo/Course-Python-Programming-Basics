n = list(map(int, input().split()))
i = 0
k = 1
while k < len(n):
    n.append(n[i])
    n.pop(i)
    k += 1
print(*n)
