def fact(a):
    if a == 0:
        return 1
    return a * fact(a - 1)


def C(n, k):
    return int(fact(n) / (fact(n - k) * fact(k)))


n = int(input())
k = int(input())
print(C(n, k))
