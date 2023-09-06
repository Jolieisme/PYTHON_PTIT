def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

test = int(input())
while test:
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    print(check(a, b))
    test -= 1
    