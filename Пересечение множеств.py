def fail(n, k):
    a = b = 0
    while 1 > 0:
        if n[a] == k[b]:
            print(n[a], end=' ')
            b += 1
            a += 1
        elif n[a] < k[b]:
            a += 1
        elif n[a] > k[b]:
            b += 1
        if a == len(n) or b == len(k):
            break


n = list(map(int, input().split()))
k = list(map(int, input().split()))
fail(n, k)
