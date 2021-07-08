n = list(map(int, input().split()))
i = 0
yes = 1
k = len(n)
while i < k - 1:
    x = n[i]
    y = n[i + 1]
    if y > x:
        yes = yes + 1
    i = i + 1
if yes == k:
    print('YES')
else:
    print('NO')
