n = str(input())
n = n.replace('', '*')
n = n[::-1]
n = n.replace('*', '', 1)
n = n[::-1]
n = n.replace('*', '', 1)
print(n)
