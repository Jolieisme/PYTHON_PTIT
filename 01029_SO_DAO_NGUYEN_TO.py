def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

test = int(input())
while test:
    number = input()
    number_reverse = number[::-1]
    if gcd(int(number), int(number_reverse)) == 1:
       print("YES")
    else:
        print("NO")
    test -= 1
    