def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
a = distance(a1, b1, c1, a2)
b = distance(a1, b1, b2, c2)
c = distance(c1, a2, b2, c2)
print('{0:.11}'.format(a + b + c))
