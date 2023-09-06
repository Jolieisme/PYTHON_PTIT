def SUM(n):
    result = 0
    for i in n:
        result += int(i)
    return result % 3 == 0

test = int(input())
while test:
    number = input()
    if SUM(number):
        print("YES")
    else:
        print("NO")
    test -= 1
