from math import *
test = int(input())
while test:
    s = input()
    tmp = 0
    result = 10 ** 19
    for i in range(0, len(s) - 1):
        if s[i].isdigit():
            tmp = tmp * 10 + int(s[i])
            if s[i+1].isalpha():
                result = min(result, tmp)
                tmp = 0
    print(result)
    test -= 1