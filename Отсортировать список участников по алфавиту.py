fail1 = open('input.txt', 'r', encoding='utf8')
fail2 = open('output.txt', 'w', encoding='utf8')
n = []
for line in fail1:
    n.append(line.split())
n.sort()
for i in range(len(n)):
    print(*n[i][:2], n[i][3], file=fail2)
fail1.close()
fail2.close()
