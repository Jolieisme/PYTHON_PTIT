test = int(input())
def check(n):
    if int(n) % 7 == 0:
        return int(n)
    result = 0
    cnt = 0
    while cnt <= 1000:
        result = (int(n) + int(n[::-1]))
        if result % 7 == 0:
           return result
        n = str(result)
        cnt += 1
    return -1

while test:
    n = input()
    print(check(n))
    test -= 1




