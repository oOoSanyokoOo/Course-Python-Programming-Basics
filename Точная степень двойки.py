n = int(input())
while n > 2:
    n /= 2
if n % 2 == 0:
    print("YES")
elif n == 1:
    print("YES")
else:
    print("NO")
