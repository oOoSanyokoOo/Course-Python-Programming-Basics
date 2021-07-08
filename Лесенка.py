n = int(input())
a = tuple(range(n))
for i in range(1, n + 1):
    for k in range(1, len(a) + 1):
        if 0 < k <= i:
            print(k, end='')
    print()
