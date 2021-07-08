n = int(input())
k = set(range(1, n + 1))
b = input()
while b != 'HELP':
    a = str(input())
    if a == "YES":
        k &= set(map(int, b.split()))
    elif a == "NO":
        k -= set(map(int, b.split()))
    b = input()
print(*sorted(k))
