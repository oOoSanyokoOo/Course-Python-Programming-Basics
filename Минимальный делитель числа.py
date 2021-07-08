def MinDivisor(n):
    i = 2
    while i <= n:
        if i * i > n:
            print(n)
            i = n + 1
        elif n % i != 0:
            i += 1
        elif n % i == 0:
            print(i)
            break


n = int(input())
MinDivisor(n)
