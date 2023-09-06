a, K, N = list(map(int, input().split()))
result = []
b = K - (a % K)
N -= a
while b <= N:
    result.append(b)
    b += K

if len(result) == 0:
    print("-1")
else:
    for i in result:
        print(i, end = " ")