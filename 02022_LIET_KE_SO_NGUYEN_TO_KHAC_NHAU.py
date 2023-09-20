from math import *
def isPrime(n):
    if  n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(sqrt(n))
    for i in range(5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = [0] * 100005
for i in a:
    b[i] += 1
for i in a:
    if isPrime(i) and b[i] > 0:
        print(i, end = " ")
        print(b[i], end = "\n")
        b[i] = 0
