fail = open('input.txt', 'r', encoding='utf-8')
n = dict()
for line in fail:
    for i in line.strip().split():
        n[i] = n.get(i, -1) + 1
        print(n[i], end=' ')
fail.close()
