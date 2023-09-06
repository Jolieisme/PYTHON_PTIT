def check(n):
    for i in range(len(n)):
        if(n[i] != '0' and n[i] != '1' and n[i] != '2'):
            return "NO"
    return "YES"

test = int(input())
while test:
    n = input()
    print(check(n))
    test -= 1