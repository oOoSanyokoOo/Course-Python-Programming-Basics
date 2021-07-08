k, m, n = int(input()), int(input()), int(input())
if k >= n:
    print(m * 2)
else:
    print(((n * 2 + (k - 1)) // k) * m)
