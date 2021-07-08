a = int(input())
m = list(map(int, input().split()))
b = int(input())
k = list(map(int, input().split()))
n = [0] * max(k)
for i in range(len(k)):
    n[k[i] - 1] += 1
for i in range(len(n)):
    if n[i] > m[i]:
        print('YES')
    else:
        print('NO')
