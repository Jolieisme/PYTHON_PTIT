from math import *

def check1(a, b):
    x = ord(a)
    y = ord(b)
    return abs(x-y) == 2

def check2(s):
    sum = 0
    for i in range(1, len(s)):
        if check1(s[i], s[i-1]):
           sum += (ord(s[i-1]) - 48)
        else:
            return "NO"
    sum += (ord(s[len(s) - 1]) - 48)
    if sum % 10 == 0:
        return "YES"
    else:
        return "NO"

test = int(input())
while test:
    s = input()
    print(check2(s))
    test -= 1
