n = list(map(int, input().split()))
k = list(map(int, input().split()))
m = 0
n.sort()
k.sort(reverse=True)
for i in range(len(n)):
    m += k[i] * n[i]
print(m)
