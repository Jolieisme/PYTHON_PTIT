def check(n):
    if len(n) % 2 == 0:
        return "NO"
    if n[0] == n[1]:
        return "NO"
    for i in range(len(n), 2):
        if n[i] != n[len(n) - 1]:
            return "NO"
    return "YES"

test = int(input())
while test:
    number = input()
    print(check(number))
    test -= 1