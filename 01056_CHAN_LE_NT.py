from math import *
def isPrime(n):
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return 0
    if n == 2 or n == 3:
        return 1
    sqr = int(sqrt(n))
    for i in range(5, sqr + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return 0
    return 1

def SUM(n):
    total = 0
    for i in n:
        total += int(i)
    return total

def check(n):
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return "NO"
    
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0:
           return "NO"
        
    if not isPrime(SUM(n)):
        return "NO"
    return "YES"

test = int(input())
while test:
    number = input()
    print(check(number))
    test -= 1
    
    