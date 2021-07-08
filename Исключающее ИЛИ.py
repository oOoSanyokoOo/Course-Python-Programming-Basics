def xor(x, y):
    if x == 0 and y == 0:
        print('0')
    elif x == 1 and y == 1:
        print("0")
    elif x == 1 or y == 1:
        print("1")

x, y = int(input()), int(input())
xor(x, y)
