from math import *
test = int(input())
while test:
    number = int(input())
    sqr = int(sqrt(number))
    print(1, end = "")
    for i in range(2, sqr + 1):
        if number % i == 0:
            cnt = 0
            while number % i == 0:
                cnt += 1
                number //= i
            print(" * ", end ="")
            print(str(i) + "^" + str(cnt), end = "")

    if number > 1:
        print(" * ", end ="")
        print(str(number) + "^" + str(1), end = "")
    print()
    test -= 1