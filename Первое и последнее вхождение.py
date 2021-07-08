n = str(input())
if 'f' in n:
    print(n.find('f'))
    b = int(n.find('f'))
    b += 1
    c1 = n[b:]
    if 'f' in c1:
        print(n.rfind('f'))
