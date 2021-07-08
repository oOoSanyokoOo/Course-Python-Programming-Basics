n = list(map(int, input().split()))
a = n[0]
k = 0
for i in range(len(n)):
    if a < n[i] > n[i - 1]:
        a, k = n[i], i
print(a, k)
