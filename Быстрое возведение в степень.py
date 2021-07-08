def power(a, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return a*power(a, n-1)
    else:
        return power(a**2, n/2)


print(power(float(input()), int(input())))
