a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

n1 = (a1 // a2) * (b1 // b2) * (c1 // c2)

n2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
n3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
n4 = (a1 // c2) * (b1 // b2) * (c1 // a2)

n5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
n6 = (a1 // b2) * (b1 // c2) * (c1 // a2)
print(max(n1, n2, n3, n4, n5, n6))
