test = int(input())
while test:
    s = input()
    sum = 0
    multy = 1
    check = False
    for i in range(len(s)):
        tmp = ord(s[i]) - ord('0')
        if i % 2 == 1:
            sum += tmp
        else:
            if tmp > 0:
                multy *= tmp
                check = True
    if check:
        print(str(multy) + " " + str(sum))
    else:
        print(str(multy) + " " + '0')
    test -= 1

