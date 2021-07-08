fail = open('input.txt', 'r', encoding='utf8')
n = [0, 0, 0]
for line in fail:
    k = int(line.split()[2])
    m = int(line.split()[3])
    if m > n[k - 9]:
        n[k - 9] = m
fail.close()
print(*n)
