def fail(num, lst):
    ls = []
    for n in range(num):
        ls.append((lst[n], n))
    return ls


a = fail(int(input()), list(map(int, input().split())))
b = fail(int(input()), list(map(int, input().split())))
a.sort()
b.sort()
k = 0
i = 0
result = [None] * len(a)
while i < len(a):
    if k + 1 == len(b) or \
            abs(a[i][0] - b[k][0]) <= abs(a[i][0] - b[k + 1][0]):
        result[a[i][1]] = b[k][1] + 1
        i += 1
    else:
        k += 1
print(*result)
