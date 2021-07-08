n, k = map(int, input().split())
m = set()
fail = set(range(1, n + 1))
for i in range(1, n + 1):
    if (i + 1) % 7 == 0:
        fail.remove(i)
    if i % 7 == 0:
        fail.remove(i)
win = set()
for i in range(k):
    a, b = map(int, input().split())
    win |= set(range(a, n + 1, b))
    win &= fail
print(len(win))
