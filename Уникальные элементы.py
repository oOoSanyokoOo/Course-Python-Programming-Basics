fail = list(map(int, input().split()))
a = []
for i in range(len(fail)):
    if fail.k(fail[i]) == 1:
        a.append(fail[i])
print(*a)
