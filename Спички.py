l1, r1, l2, r2, l3, r3 = int(input()), int(input()), int(input()), \
                         int(input()), int(input()), int(input())
if (l1 <= l2 <= r1 and l2 <= l3 <= r2) or \
        (l1 <= l3 <= r1 and l3 <= l2 <= r3) or \
        (l2 <= l1 <= r2 and l1 <= l3 <= r1) or \
        (l2 <= l3 <= r2 and l3 <= l1 <= r3) or \
        (l3 <= l1 <= r3 and l1 <= l2 <= r1) or \
        (l3 <= l2 <= r3 and l2 <= l1 <= r2) or \
        (l1 <= l2 and l1 <= l3 and r1 >= r2 and r1 >= r3) or \
        (l2 <= l1 and l2 <= l3 and r2 >= r1 and r2 >= r3) or \
        (l3 <= l2 and l3 <= l1 and r3 >= r2 and r3 >= r1):
    print(0)
elif 0 < l2 - r3 <= r1 - l1 or 0 < l3 - r2 <= r1 - l1 or l2 <= l3 <= r2 or \
     l3 <= l2 <= r3:
    print(1)
elif 0 < l1 - r3 <= r2 - l2 or 0 < l3 - r1 <= r2 - l2 or l1 <= l3 <= r1 or \
     l3 <= l1 <= r3:
    print(2)
elif 0 < l1 - r2 <= r3 - l3 or 0 < l2 - r1 <= r3 - l3 or l1 <= l2 <= r1 or \
     l2 <= l1 <= r2:
    print(3)
else:
    print(-1)
