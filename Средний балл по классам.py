fail = open('input.txt', 'r', encoding='utf8')
n, k = [0, 0, 0], [0, 0, 0]
for line in fail:
    m = line.split()
    n[int(m[2]) - 9] += 1
    k[int(m[2]) - 9] += int(m[3])
print(' '.join(map(lambda x: str(k[x] / n[x]), range(0, 3))))
fail.close()
