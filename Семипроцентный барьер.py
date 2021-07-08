fail = open('input.txt', 'r', encoding='utf8')
a, n, r = [], [], []
k, i = 0, 1
c = fail.readlines()
while c[i].strip() != 'VOTES:':
    a.append(c[i].strip())
    i += 1
for j in range(len(c)):
    n.append(c[j].strip())
for j in range(len(a)):
    r.append((a[j], n.count(a[j]) - 1))
    k += n.count(a[j]) - 1
for s in range(len(a)):
    if r[s][1] / k * 100 >= 7:
        print(r[s][0])
