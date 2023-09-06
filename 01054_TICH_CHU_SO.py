def Multy(n):
    result = 1
    for i in n:
        if i == '0':
            result = result
        else:
            result *= int(i)
    return result

test = int(input())
while test:
    number = input()
    print(Multy(number))
    test -= 1
