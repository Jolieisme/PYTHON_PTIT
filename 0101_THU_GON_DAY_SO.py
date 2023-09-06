n = int(input())
list_num = list(map(int, input().split()))
result = []

for i in list_num:
    if len(result) == 0:
        result.append(i)
    else:
        if (result[-1] + i) % 2 == 0:
            result.pop()
        else:
            result.append(i)
print(len(result))
 