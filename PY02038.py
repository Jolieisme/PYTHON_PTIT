from math import *

n = int(input())
a = []
cnt = 0
ans = 0
for i in range(n):
        s = input()
        a.append(s)
for line in a:
    for i in line:
        if i == 'C':
            cnt += 1
    ans += comb(cnt, 2)
    cnt = 0

for i in range(n):
    for j in range(n):
        if a[j][i] == 'C':
            cnt += 1
    ans += comb(cnt, 2)
    cnt = 0

print(ans)



