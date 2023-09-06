test = int(input())
f = [1] * 10
for i in range(2, 10):
    f[i] = f[i-1] * i

while test:
    s = input()
    sum = 0
    for i in s:
       sum += f[int(i)]
    
    if sum == int(s):
        print("Yes")
    else:
        print("No")
    test -= 1