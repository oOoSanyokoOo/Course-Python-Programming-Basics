n = str(input())
n = n.replace('h', 'H')
n = n[::-1]
n = n.replace('H', "h", 1)
n = n[::-1]
n = n.replace('H', "h", 1)
print(n)
