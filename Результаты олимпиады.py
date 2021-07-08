a = int(input())
i = 0
n = []
while i < a:
    m = list(input().split())
    i = i + 1
    n.append(m)
n.sort(key=lambda n: (-1 * int(n[1])))
for i in n:
    print(*i[0], sep='')
