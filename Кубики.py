inFile = open('input.txt', 'r', encoding='utf-8')
n, m = map(int, inFile.readline().split())
a = set()
k = set()
while len(a) < n:
    a.add(int(inFile.readline()))
while len(k) < m:
    k.add(int(inFile.readline()))
print(len(a & k))
print(*sorted(a & k))
print(len(a - k))
print(*sorted(a - k))
print(len(k - a))
print(*sorted(k - a))
inFile.close()
