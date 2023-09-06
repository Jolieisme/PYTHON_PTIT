from math import *
N , K = list(map(int, input().split()))
start = 10 ** (K-1)
end = 10 ** K
cnt = 0
for i in range(start, end):
    if gcd(i, N) == 1:
        print(i, end = " ")
        cnt += 1
        if cnt % 10 == 0:
           print()
