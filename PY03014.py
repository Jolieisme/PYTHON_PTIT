test = int(input())
while test:
    res = []
    s = input()
    cnt = 1
    for i in s:
        if i == '(':
            print(cnt, end=' ')
            res.append(cnt)
            cnt += 1
        elif i == ')':
            print(res.pop(), end=' ')
    print()
    test -= 1