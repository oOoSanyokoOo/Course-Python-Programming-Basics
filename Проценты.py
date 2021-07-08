p, x, y = float(input()) / 100, int(input()) * 100, int(input())
k = x + y
v = k * p
print(int((k + v) / 100), int((k + v) % 100))
