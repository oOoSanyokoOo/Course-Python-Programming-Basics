def CountSort(m):
    n = max(m)
    k = [0] * (n + 1)
    for i in m:
        k[i] = k[i] + 1
    for j in range(n + 1):
        print((str(j) + ' ') * k[j], end='')


m = list(map(int, input().split()))
CountSort(m)
