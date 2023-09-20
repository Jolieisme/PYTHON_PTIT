test = int(input())
while test:
    n = int(input())
    b = [0]*1000005
    a = list(map(int, input().split()))
    for i in a:
        b[i] += 1
    MIN = 10**6
    for i in set(a):
        if(b[i] > n/2):
            MIN = min(i, MIN)
    if(MIN == 10**6):
        print("NO")
    else:
        print(MIN)
    test -= 1