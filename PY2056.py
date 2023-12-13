n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
    for j in x:
        tmp1 = str(j)
        tmp2 = str(j)[::-1]
        if tmp1 == tmp2 and len(tmp1) > 1:
            b.append(j)
ans = 0
if len(b) == 0:
    print("NOT FOUND")
else:
    ans = max(b)
    result = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans:
                result.append(f'Vi tri [{i}][{j}]')

    print(ans)
    for i in result:
        print(i)








