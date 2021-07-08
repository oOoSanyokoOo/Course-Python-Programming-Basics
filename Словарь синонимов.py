n = int(input())
fail = dict(input().split() for j in range(n))
m = input()
for k, j in fail.items():
    if m == k:
        print(j)
    if m == j:
        print(k)
