n = int(input())
num = [int(i) for i in input().split()]
cnt = 0

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if(num[i] > num[j]):
            cnt += 1
print(cnt)

