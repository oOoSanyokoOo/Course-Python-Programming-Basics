n = int(input())
print((n // 1000 + n % 1000 // 100 * 10) - (n % 10 + n % 100 // 10 * 10) + 1)
