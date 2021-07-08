s, k, s1, k1 = int(input()), int(input()), int(input()), int(input())
if (s + k) % 2 == (s1 + k1) % 2 == 0:
    if k1 >= k + abs(s1 - s):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
