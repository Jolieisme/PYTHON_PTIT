test = int(input())
nice_number_list = []
def check(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

x = 2
while x <= 888:
    if check(str(x)):
        tmp = str(x)
        nice_number_list.append(tmp + tmp[::-1])
    x += 2

while test:
    num = input()
    for i in nice_number_list:
        if int(i) > int(num):
            break
        print(i, end = " ")
    print()
    test -= 1

