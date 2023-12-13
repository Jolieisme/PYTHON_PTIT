num = input()
while len(num) > 1:
    x = num[:len(num)//2:]
    y = num[len(num)//2 ::]
    num = str(int(x) + int(y))
    print(num)


