a = int(input())
n = list(map(int, input().split()))
n.sort()
k = 0
for i in n:
    if i >= a:
        k += 1
        a = i + 3
print(k)
