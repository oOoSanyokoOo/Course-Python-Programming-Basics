fail = list(map(int, input().split()))
n, k = 0, 0
for i in fail:
    if fail.count(i) > n:
        n = fail.count(i)
        k = i
print(k)
