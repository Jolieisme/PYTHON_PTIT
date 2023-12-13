import math
n = int(input())
a = []
duoi = 0
tren = 0
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
k = int(input())
for i in range(n):
    for j in range(n):
        if i > j:
            duoi += a[i][j]
        elif j > i:
            tren += a[i][j]
res = abs(tren - duoi)
if res <= k:
    print("YES")
else:
    print("NO")
print(res)