a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == b == c == d == e == f == 0:
    print(5)
elif a * d == b * c and a * f != c * e:
    print(0)
elif a == b == 0 and e != 0:
    print(0)
elif c == d == 0 and f != 0:
    print(0)
elif a == c == 0 and b * f != d * e:
    print(0)
elif b == d == 0 and a * f != c * e:
    print(0)
elif a * d == b * c and a * f == c * e:
    if b == d == 0:
        if a != 0 and c != 0:
            print(3, e / a)
        elif a == e == 0:
            print(3, f / c)
        elif c == f == 0:
            print(3, e / a)
    elif a == c == 0:
        if b != 0:
            print(4, e / b)
        elif d != 0:
            print(4, f / d)
    elif b != 0:
        print(1, -a / b, e / b)
    elif d != 0:
        print(1, -c / d, f / d)
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print(2, x, y)
