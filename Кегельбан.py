n, k = map(int, input().split())
fail = list('I' * n)
for i in range(k):
    l, r = map(int, input().split())
    while l <= r:
        fail.pop(l - 1)
        fail.insert(l - 1, '.')
        l += 1
print(''.join(fail))
