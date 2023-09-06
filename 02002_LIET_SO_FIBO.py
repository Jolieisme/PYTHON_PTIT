f = [0] * 95
f[1] = 1
f[2] = 1
for i in range(3, 93):
    f[i] = f[i-1] + f[i-2]

test = int(input())
while test:
    start, end = list(map(int, input().split()))
    for i in range(start, end + 1):
        print(f[i], end = " ")
    print()
    test -= 1