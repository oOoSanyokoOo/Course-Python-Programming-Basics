fail = open('input.txt', 'r', encoding='utf-8')
n = []
m = []
fail.readline()
for line in fail:
    if line != 'VOTES:\n':
        n.append(line.strip())
    else:
        break
for line in fail:
    m.append(line.strip())
k = []
for i in range(len(n)):
    k.append((-m.count(n[i]), n[i]))
k.sort()
for i in k:
    print(i[1])
