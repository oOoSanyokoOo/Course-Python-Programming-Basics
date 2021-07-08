a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
else:
    if c * (-b / a) + d != 0 and (int(-b / a) == -b / a):
        print(int(-b / a))
    else:
        print('NO')
