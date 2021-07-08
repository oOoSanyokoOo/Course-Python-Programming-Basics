fail = open('input.txt', 'r', encoding='utf8')
n = []
a = []
b = []
for line in fail:
    k = line.split()[2]
    m = int(line.split()[3])
    if k == '9':
        n.append(m)
    if k == '10':
        a.append(m)
    if k == '11':
        b.append(m)
n.sort(reverse=True)
for i in n:
    if i < max(n):
        print(i, end=' ')
        break
a.sort(reverse=True)
for i in a:
    if i < max(a):
        print(i, end=' ')
        break
b.sort(reverse=True)
for i in b:
    if i < max(b):
        print(i)
        break
fail.close()
