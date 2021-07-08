n = int(input())
if 10 < n < 20 or n % 10 >= 5 or n % 10 == 0:
    print(f"{n} korov")
elif n % 10 == 1 and n != 11:
    print(f"{n} korova")
else:
    print(f"{n} korovy")
