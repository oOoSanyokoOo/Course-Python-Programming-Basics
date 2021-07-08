n, m, k = int(input()), int(input()), int(input())
if (k % n == 0 or k % m == 0) and n * m > k:
    print("YES")
else:
    print("NO")
