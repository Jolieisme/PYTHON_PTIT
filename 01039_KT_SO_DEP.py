def check(s):
    if(s[0] == s[1]):
        return "NO"
    for i in range(2, len(s)):
        if s[i] != s[i % 2 == 1]: 
            return "NO"
    return "YES"

test = int(input())
while test:
    s = input()
    print(check(s))
    test -= 1
    