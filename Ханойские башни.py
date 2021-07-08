def fail(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        fail(n - 1, x, 6 - x - y)
        print(n, x, y)
        fail(n - 1, 6 - x - y, y)


n = int(input())
fail(n, 1, 3)
