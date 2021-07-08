h, a, b = int(input()), int(input()), int(input())
print(((h - b) // (a - b)) + (((h - b) % (a - b)) > 0))
