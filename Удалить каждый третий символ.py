n = input()
i = 0
a = n
while i <= len(n) - 1:
    if i % 3 == 0:
        a = a.replace(a[a.find(n[i])], '', 1)
    i += 1
print(a)
