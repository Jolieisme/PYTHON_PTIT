from math import *
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], end = " ")
            print(a[j], end = "\n")

        
        