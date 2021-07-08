a = int(input())
b = int(input())
for i in range(a, b + 1):
    k = str(i)
    if str(i // 100) == k[3] + k[2]:
        print(i)
