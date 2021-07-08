n = list(map(int, input().split()))
k = []
for i in n:
    if i in k:
        continue
    k.append(i)
print(len(k))
