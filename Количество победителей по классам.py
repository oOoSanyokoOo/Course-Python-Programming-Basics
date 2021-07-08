fail = open('input.txt', 'r', encoding='utf8')
n = []
a = []
i = []
for line in fail:
    k = line.split()[2]
    m = int(line.split()[3])
    if k == '9':
        n.append(m)
    if k == '10':
        a.append(m)
    if k == '11':
        i.append(m)
print(n.count(max(n)), a.count(max(a)), i.count(max(i)))
fail.close()
