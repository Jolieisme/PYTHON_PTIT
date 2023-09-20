from math import *
n = int(input())
a = list(map(float, input().split()))
a.sort()
sum = 0
cnt = 0
for i in range(len(a)):
    if a[i] != a[0] and a[i] != a[len(a) - 1]:
        sum += a[i]
        cnt += 1
print('{:.2f}'.format(sum / cnt))
        