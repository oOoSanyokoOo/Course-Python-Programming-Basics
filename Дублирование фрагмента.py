n = str(input())
a = n.find("h")
b = n.rfind('h')
print(f'{n[:b]}{n[a + 1:]}')
