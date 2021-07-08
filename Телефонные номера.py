n = input()
a = input()
b = input()
c = input()
w = dict()
k = 0
myList = [n, a, b, c]
for i in myList:
    fail = ''
    k += 1
    for sym in i:
        if sym.isdigit():
            fail += sym
    if len(fail) == 7:
        fail = '495' + fail
    else:
        fail = fail[1:]
    w[k] = fail
    if k >= 2:
        if w[1] == w[k]:
            print('YES')
        else:
            print('NO')
