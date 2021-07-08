s = str(input())
if s.find('f') == -1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
