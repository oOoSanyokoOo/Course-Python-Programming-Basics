p = int(input())
x = int(input())
y = int(input())
k = int(input())
while k > 0:
    s = (x * 100 + y) * (100 + p) / 100
    x = int(s // 100)
    y = int(s % 100)
    k -= 1
print(x, y)
