fail = list(map(int, input().split()))
a = min(fail)
b = fail.index(a)
с = max(fail)
d = fail.index(с)
fail[b], fail[d] = fail[d], fail[b]
print(*fail)
