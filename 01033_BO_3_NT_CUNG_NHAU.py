from math import *
L, R = list(map(int, input().split()))

for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        for z in range(j + 1, R + 1):
            if gcd(i, j) == 1 and gcd(j,z) == 1 and gcd(i, z) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(z) + ")")
