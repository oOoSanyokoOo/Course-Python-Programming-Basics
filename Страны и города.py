n = int(input())
fail = {}
for i in range(n):
    a = input().split()
    for j in range(1, len(a)):
        fail[a[j]] = a[0]
k = int(input())
for i in range(k):
    print(fail[input()])
