from math import *
n = int(input())
a = list(map(int, input().split()))
mark = [0] * 505
b = []

for i in a:
    mark[i] += 1

for i in a:
    if mark[i] > 0:
        b.append(i)
        mark[i] = 0
def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

for i in range(1, len(b)):
    b[i] += b[i-1]

check = False
for i in range(len(b)):
    if isPrime(b[i]) and isPrime(b[len(b) - 1] - b[i]):
        check = True
        print(i)
        break

if not check:
    print("NOT FOUND")
