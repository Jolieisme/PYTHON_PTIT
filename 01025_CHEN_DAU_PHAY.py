s1 = input()
s2 = s1[::-1] 
result = ""
cnt = 0
for i in s2:
    if cnt == 3:
        result += ' ,'
        cnt = 0
    result += i
    cnt += 1

print(result[::-1])
