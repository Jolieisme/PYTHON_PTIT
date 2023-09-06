def check(n):
    if len(n) % 2 != 0 or n != n[::-1]:
        return 0
    for i in n:
        if int(i) % 2 == 1:
            return 0
    return 1

test = int(input())
while test:
    n = int(input())
    for i in range(22, n, 2):
        if(check(str(i))):
            print(i, end = " ")
    print()
    test -= 1