n = list(map(int, input().split()))
a = [i for i in n if i % 2 != 0]
print(min(a))
