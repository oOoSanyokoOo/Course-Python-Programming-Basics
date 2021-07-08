fail = open('input.txt', 'r', encoding='utf-8')
result = open('output.txt', 'w', encoding='utf-8')
n = []
k = int(fail.readline())
for line in fail:
    m = line.split()
    if int(m[-1]) > 39 and int(m[-2]) > 39 and int(m[-3]) > 39:
        n.append(int(m[-1]) + int(m[-2]) + int(m[-3]))
n.sort(reverse=True)
if len(n) <= k:
    print(0)
elif n.count(n[0]) > k:
    print(1)
elif n[k:].count(n[k - 1]) < 1:
    print(n[:k][-1])
else:
    print(n[:n.index(n[k - 1])][-1])
fail.close()
