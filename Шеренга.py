n = list(map(int, input().split()))
a = int(input())
b = []
for i in range(len(n)):
    if n[i] >= a:
        b.append(n[i])
print(len(b) + 1)
