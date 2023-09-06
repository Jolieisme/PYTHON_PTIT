test = int(input())
while test:
    n, d = list(map(int, input().split()))
    list_num = [int(i) for i in input().split()]
    # for i in list_num:
    #     print(i, end = ' '
    
    for i in range(d, len(list_num)):
        print(list_num[i], end = " ")
    
    for i in range(0, d):
        print(list_num[i], end = " ")
    print()
    test -= 1