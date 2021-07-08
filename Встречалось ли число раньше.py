n = list(map(int, input().split()))
m = set()
for i in n:
    if i in m:
        print('YES')
    elif i not in m:
        print('NO')
    m.add(i)
