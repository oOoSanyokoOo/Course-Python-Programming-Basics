n = list(map(int, input().split()))
i = 1
k = 0
while i < len(n) - 1:
    if n[i] > n[i + 1] and n[i] > n[i - 1]:
        k += 1
    i += 1
print(k)
