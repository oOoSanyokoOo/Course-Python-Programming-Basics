fail = open('input.txt', 'r', encoding='utf8')
n = {}
for line in fail:
    k = line.split()
    n[k[0]] = n.get(k[0], 0) + int(k[1])
for name, votes in sorted(n.items()):
    print(name, votes)
