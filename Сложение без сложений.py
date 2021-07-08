def sum(a, b):
    i = 0
    if a == 0:
        return b
    if b == 0:
        return a
    if a > 0:
        i += 1
        return sum(a, b - 1) + i


a = int(input())
b = int(input())
print(sum(a, b))
