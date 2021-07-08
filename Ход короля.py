n1, s1, n2, s2 = int(input()), int(input()), int(input()), int(input())
if n2 == n1 + 1 and s2 == s1 + 1:
    print("YES")
elif n2 == n1 + 0 and s2 == s1 + 1:
    print("YES")
elif n2 == n1 - 1 and s2 == s1 + 1:
    print("YES")
elif n2 == n1 - 1 and s2 == s1 + 0:
    print("YES")
elif n2 == n1 - 1 and s2 == s1 - 1:
    print("YES")
elif n2 == n1 + 0 and s2 == s1 - 1:
    print("YES")
elif n2 == n1 + 1 and s2 == s1 - 1:
    print("YES")
elif n2 == n1 + 1 and s2 == s1 + 0:
    print("YES")
else:
    print("NO")
