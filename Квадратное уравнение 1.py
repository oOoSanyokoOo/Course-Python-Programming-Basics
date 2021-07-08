import math
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d > 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
if d == 0:
    print(-b/(2*a))
elif d > 0 and x1 > x2:
    print(x2, x1)
elif d > 0 and x1 < x2:
    print(x1, x2)
