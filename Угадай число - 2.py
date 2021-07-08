fail = open('input.txt', 'r', encoding='utf8')
a = fail.readlines()
n = int(a[0])
b = set([i for i in range(1, n + 1)])
for j in range(1, len(a) - 1):
    k = set(map(int, a[j].split()))
    if len(k & b) <= len(b) // 2:
        print('NO')
        b -= k
    elif len(k & b) > len(b) // 2:
        print('YES')
        b &= k
b = list(b)
b.sort()
print(*b)
