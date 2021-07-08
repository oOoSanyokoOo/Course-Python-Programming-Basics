def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
