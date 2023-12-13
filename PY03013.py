test = int(input())

def cnt_digit(a, b):
    digit_count = {str(i): 0 for i in range(10)}
    for num in range(a, b+1):
        num_str = str(num)
        for digit in num_str:
            digit_count[digit] += 1
    return digit_count

while test:
    a, b = map(int, input().split())
    res = cnt_digit(a, b)
    for item in res.items():
        print(item[1], end=' ')
    print()
    test -= 1
