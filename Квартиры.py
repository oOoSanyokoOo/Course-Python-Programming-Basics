x, y = int(input()), int(input())
if y % (y - x + 1) == 0:
    print("YES")
else:
    print("NO")
