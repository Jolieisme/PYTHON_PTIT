class number:
    def __init__(self, val):
        self.val = val
        self.sumDigit = 0
        while val > 0:
            self.sumDigit += val % 10
            val //= 10

def cmp(a):
    return (a.sumDigit, a.val)


test = int(input())
while test:
    n = input()
    a = list(map(int, input().split()))
    result = []
    for i in a:
        result.append(number(i))
    result.sort(key= cmp)
    for i in result:
        print(i.val, end = " ")
    print()
    test -= 1
    