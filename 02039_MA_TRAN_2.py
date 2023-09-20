n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())

nuaTren = 0
nuaDuoi = 0
for i in range(n):
    for j in range(n):
        if j > n - i - 1:
            nuaTren += a[i][j]
        elif j < n - i - 1:
            nuaDuoi += a[i][j]

if abs(nuaTren - nuaDuoi) <= k:
    print("YES")
else:
    print("NO")

print(abs(nuaTren - nuaDuoi))