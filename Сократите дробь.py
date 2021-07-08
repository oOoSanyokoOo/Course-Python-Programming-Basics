def func(a, b):
    if a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    elif a > b:
        return a
    else:
        return b
    return func(a, b)


a, b = int(input()), int(input())
d = func(a, b)
print(a//d, b//d)
