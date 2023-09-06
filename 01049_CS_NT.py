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

def check_num(n):
    cnt = 0
    if not isPrime(len(n)):
        return 0
    for i in n:
        if isPrime(int(i)):
            cnt += 1
    if cnt < len(n) - cnt:
        return 0
    return 1

test = int(input())
while test:
    n = input()
    if check_num(n):
        print("YES")
    else:
        print("NO")
    test -= 1