s = input()
k = int(input())
m = []
check = 0
mark = [0] * 10005
for i in range(0, len(s), 2):
    x = int(s[i:i + 2])
    if x >= 10:
        m.append(x)
        mark[x] += 1
m.sort()
for i in m:
    if mark[i] >= k:
        check = 1
        print(i, end=" ")
        print(mark[i], end="\n")
        mark[i] = 0
if not check:
    print("NOT FOUND")

