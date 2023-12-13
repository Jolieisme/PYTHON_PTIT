n,m = map(int, input().split())
a = []
res = []
MIN, MAX = 1000, 0
mark = 0
# def check(n):
#     if n == 2 or n == 3:
#         return 1
#     if n < 2 or n % 2 == 0 or n % 3 == 0:
#         return 0
#     sqr = sqrt(n)
#     i = 5
#     while i <= sqr:
#         if n % i == 0 or n % (i+2) == 0:
#             return 0
#         i += 6
#     return 1

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
    MIN = min(MIN, min(x))
    MAX = max(MAX, max(x))

y = MAX - MIN
for i in range(n):
    for j in range(m):
        if a[i][j] == y:
            res.append(f'Vi tri [{i}][{j}]')

if len(res) == 0:
    print("NOT FOUND")
else:
    print(y)
    for i in res:
        print(i)



