n = [int(i) for i in input().split()]
print(*[n[i + 1] for i in range(len(n) - 1) if n[i] < n[i + 1]], sep=' ')
