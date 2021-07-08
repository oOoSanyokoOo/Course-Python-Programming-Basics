n = list(map(int, input().split()))
k = []
for i in n:
    if i > 0:
        k += [i]
print(min(k))
