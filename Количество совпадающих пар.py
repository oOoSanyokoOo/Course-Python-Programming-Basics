fail = list(map(int, input().split()))
n = 0
for i in range(len(fail)):
    for c in range(1, len(fail) - i):
        if fail[i] == fail[i + c]:
            n += 1
print(n)
