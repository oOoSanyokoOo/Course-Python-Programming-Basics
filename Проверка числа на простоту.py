def IsPrime(n):
    i = 2
    a = False
    while i <= n ** 0.5:
        if n % i == 0:
            return a
        i += 1
    return not (a)


n = int(input())
if n == 2 or IsPrime(n):
    print('YES')
else:
    print('NO')
