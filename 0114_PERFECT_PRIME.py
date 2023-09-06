from math import *
test = int(input())
def isPrime(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    sqr = int(sqrt(n))
    for i in range(5, sqr, 6):
        if n % i == 0:
            return 0
    return 1
 
def check(n):
    sum = 0
    if not isPrime(int(n)):
        return "No"
    if not isPrime(int(n[::-1])):
        return "No"
    
    for i in n:
        tmp = ord(i) - 48
        sum += (tmp)
        if not isPrime(tmp):
            return "No"
    if not isPrime(sum):
        return "No"
    return "Yes"

while test:
    n = input()
    print(check(n))
    test -= 1
