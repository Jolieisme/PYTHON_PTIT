test = int(input())
def check(n):
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return "NO"
    return "YES"

while test:
    num = input()
    print(check(num))
    test -= 1

