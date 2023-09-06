from math import *
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def sum_digit(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    sqr = sqrt(n)
    while i <= sqr:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

test = int(input())
while test:
    a, b = list(map(int, input().split()))
    if isPrime(sum_digit(gcd(a, b))):
        print("YES")
    else:
        print("NO")
    test -= 1
    