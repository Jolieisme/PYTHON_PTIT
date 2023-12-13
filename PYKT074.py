test = int(input())
while test:
    s = input().split()
    cnt = 0
    for i in s:
        if cnt + len(i) <= 100:
            print(i, end=" ")
            cnt += len(i) + 16
        else:
            break

    print()
    test -= 1