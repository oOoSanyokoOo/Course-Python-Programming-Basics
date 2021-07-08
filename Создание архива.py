n = list(map(int, input().split()))
k = []
for i in range(n[1]):
    k.append(int(input()))
if n[0] >= sum(k):
    print(n[1])
else:
    while n[0] < sum(k):
        k.pop(k.index(max(k)))
    print(len(k))
