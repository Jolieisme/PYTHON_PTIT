from math import *
test = int(input())
while test:
    n, x, m = list(map(float, input().split()))
    x /= 100
    result = log(m/n, 1+x)
    if result == int(result):
        print(int(result))
    else:
        print(int(result) + 1)
    test -= 1
