fail = list(map(int, input().split()))
n = fail.copy()
if len(fail) > 3:
    c1 = max(fail)
    fail.remove(max(fail))
    c2 = max(fail)
    fail.remove(max(fail))
    c3 = max(fail)
    d1 = min(n)
    n.remove(min(n))
    d2 = min(n)
    n.remove(min(n))
    d3 = min(n)
    if d1 * d2 * c1 > c1 * c2 * c3:
        print(d1, d2, c1)
    else:
        print(c1, c2, c3)
else:
    print(*fail)
