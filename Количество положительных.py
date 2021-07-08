n = input().split()
k = 0
for i in range(0, len(n)):
    if int(n[i]) > 0:
        k = k + 1
print(k)
