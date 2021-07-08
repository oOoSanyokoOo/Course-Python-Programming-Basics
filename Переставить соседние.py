fail = input().split()
for i in range(0, len(fail) // 2 * 2, 2):
    fail[i], fail[i + 1] = fail[i + 1], fail[i]
print(*fail)
