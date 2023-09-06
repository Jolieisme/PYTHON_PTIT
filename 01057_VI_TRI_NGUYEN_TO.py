from math import *
def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3  == 0:
        return 0
    sqr = int(sqrt(n))
    for i in range(5, sqr + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return  0
    return 1


def check(n):
    for i in range(0, len(s)):
        tmp = ord(s[i]) - ord('0')
        if isPrime(i) and not isPrime(tmp):
            return 0
        if not isPrime(i) and isPrime(tmp):
            return 0
    return 1

test = int(input())
while test:
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
    test -= 1
    