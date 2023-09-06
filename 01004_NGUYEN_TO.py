from math import *
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    sqr = sqrt(n)
    i = 5
    while i <= sqr:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

test = int(input())
while test:
    num = int(input())
    cnt = 0
    for i in range(1, num):
        if gcd(num, i) == 1:
           cnt += 1
    if isPrime(cnt):
        print("YES")
    else:
        print("NO")
    test -= 1


