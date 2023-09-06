from math import *
def isPrime(n):
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return "NO"
    if n == 3 or n == 2:
        return "YES"
    sqr = int(sqrt(n))
    for i in range(5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "NO"
    return "YES"

def SUM(n):
    result = 0
    for i in n:
        result += int(i)
    return result


test = int(input())
while test:
    number = input()
    answer = SUM(number)
    print(isPrime(answer))
    test -= 1

    