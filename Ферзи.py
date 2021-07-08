fail = []
k = 0
for i in range(8):
    x, y = map(int, input().split())
    fail.append(x)
    fail.append(y)
i = 0
while i < 13:
    j = i + 1
    n = 2
    while n < (15 - i):
        if abs(fail[i] - fail[i + n]) == abs(fail[j] - fail[j + n]):
            k += 1
        if fail[i] - fail[i + n] == 0 or fail[j] - fail[j + n] == 0:
            k += 1
        n += 2
    i += 2
if k > 0:
    print('YES')
else:
    print('NO')
