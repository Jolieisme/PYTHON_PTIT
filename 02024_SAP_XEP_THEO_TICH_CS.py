class number:
    def __init__(self, val):
        self.val = val
        self.multi_digit = 1
        while val > 0:
            self.multi_digit *= val % 10
            val //= 10

def cmp(a):
    return(a.multi_digit, a.val)

test = int(input())
while test:
    n = input()
    a = list(map(int, input().split()))
    result = []
    for i in a:
        result.append(number(i))
    result.sort(key=cmp)
    for i in result:
        print(i.val, end = " ")
    print()
    test -= 1