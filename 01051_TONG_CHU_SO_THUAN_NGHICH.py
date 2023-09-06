def check(n):
    result = 0
    for i in n:
        result += int(i)
    tmp = str(result)
    if tmp == tmp[::-1] and result > 9:
        return "YES"
    return "NO"

test = int(input())
while test:
    number = input()
    print(check(number))
    test -= 1

