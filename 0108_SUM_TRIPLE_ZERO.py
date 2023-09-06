test = int(input())
while test:
    n = int(input())
    a = list(map(int, input().split()))
    MIN = 10 ** 9
    for i in range(0, n    ):
        l = i + 1
        r = len(a) - 1
        while l < r:
            MIN = min(MIN, a[i] + a[l] + a[r])
            l += 1
    print(MIN)
    test -= 1
            

