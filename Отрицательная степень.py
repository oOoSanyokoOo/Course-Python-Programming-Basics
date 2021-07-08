def power(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1
    for i in range(abs(n)-1):
        a *= b
    if n < 0:
        return 1/a
    else:
        return a


b, s = float(input()), int(input())
print(power(b, s))
