n = int(input())
print('+___ ' * n, sep='')
for i in range(n):
    print('|', i + 1, ' / ', sep='', end='')
print()
print('|__\\ ' * n, sep='')
print('|    ' * n, sep='')
