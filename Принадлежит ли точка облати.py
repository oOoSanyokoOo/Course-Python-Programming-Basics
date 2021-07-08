def IsPointArea(x, y):
    return (x + 1) ** 2 + (y - 1) ** 2 - 4 <= 0 and \
            y + x >= 0 and 2 * x + 2 - y <= 0 \
            or (x + 1) ** 2 + (y - 1) ** 2 - 4 >= 0 and \
            y + x <= 0 and 2 * x + 2 - y >= 0


x, y = float(input()), float(input())
if IsPointArea(x, y):
    print('YES')
else:
    print('NO')
