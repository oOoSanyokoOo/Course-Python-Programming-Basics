n = str(input())
a = n.find("h")
b = n.rfind('h')
print(n[:a] + n[b + 1:])
