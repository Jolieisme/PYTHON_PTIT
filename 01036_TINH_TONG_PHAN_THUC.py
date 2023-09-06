from math import *
test = int(input())
while test:
    N = int(input())
    sum = 0.0
    if N % 2 == 1:
        for i in range(1, N+1, 2):
            sum += float(1 / i)

    else:
        for j in range(2, N+1, 2):
            sum += float(1 / j)

    print("{:.6f}".format(sum))
    test -= 1
