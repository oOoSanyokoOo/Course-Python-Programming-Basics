first, midle, now = int(input()), int(input()), int(input())
d = 0
point1 = 0
point2 = 1
while now != 0:
    point2 += 1
    if first < midle and midle > now:
        if point1 == 0:
            point1 = point2
        elif d == 0 or d > point2 - point1:
            d = point2 - point1
        point1 = point2
    first, midle, now = midle, now, int(input())
print(d)
