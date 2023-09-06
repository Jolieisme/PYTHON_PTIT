test = int(input())
while test:
    s = input()
    if s[0] == s[len(s) - 1]:
        print("YES")
    else:
        print("NO")
    test -= 1