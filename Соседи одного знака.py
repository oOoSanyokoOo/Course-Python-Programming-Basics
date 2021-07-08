n = list(map(int, input().split()))
i = 0
while i < len(n) - 1:
    if (n[i] > 0 and n[i + 1] > 0) or (n[i] < 0 and n[i + 1]) < 0:
        print(n[i], n[i + 1])
        break
    i += 1
