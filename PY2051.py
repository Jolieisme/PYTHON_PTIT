n = int(input())
b = []
for i in range(n):
    x = list(map(int, input().split()))
    b.append(x)

if n == 2:
    print(str(b[0][1] // 2) + " " + str(b[0][1]//2))
else:
    result = []
    result.append((b[0][1] + b[0][2] - b[1][2])//2)
    for i in range(1, n):
        result.append(b[0][i] - result[0])
    for i in result:
        print(i, end = " ")
