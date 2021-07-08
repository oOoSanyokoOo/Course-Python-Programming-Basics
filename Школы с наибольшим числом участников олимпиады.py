fail = open('input.txt', 'r', encoding='utf8')
n = [0] * 100
for line in fail:
    k = line.split()
    n[int(k[2])] += 1
m = max(n)
for i in range(len(n)):
    if n[i] == m:
        print(i, end=' ')
fail.close()
