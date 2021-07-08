fail = list(map(int, input().split()))
n = 0
for i in tuple(fail):
    if i != 0:
        n += 1
    elif i == 0:
        k = fail.pop(n)
        fail.append(k)
print(*fail)
