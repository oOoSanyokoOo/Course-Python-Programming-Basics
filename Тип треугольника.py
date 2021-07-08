a, b, c = int(input()), int(input()), int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if a < b + c:
    if a * a == b * b + c * c:
        print('rectangular')
    elif a * a < b * b + c * c:
        print('acute')
    elif a * a > b * b + c * c:
        print('obtuse')
else:
    print('impossible')
