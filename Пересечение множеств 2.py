a, b = set(list(map(int, input().split()))), \
       set(list(map(int, input().split())))
print(*sorted(a & b))
