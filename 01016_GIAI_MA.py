test = int(input())
while test:
    s = input()
    i = 1
    while i <= len(s):
        tmp = int(s[i])
        while tmp:
           print(s[i-1], end ='')
           tmp -= 1
        i += 2
    print()
    test -= 1