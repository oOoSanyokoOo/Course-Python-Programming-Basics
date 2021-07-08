n = list(map(int, input().split()))
a = min(n)
b = max(n)
n.remove(a)
n.remove(b)
с = min(n)
d = max(n)
if a * с > b * d:
    print(min(с, a), max(с, a))
else:
    print(min(d, b), max(d, b))
