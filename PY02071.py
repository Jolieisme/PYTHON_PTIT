res = []

def Try(i, sum, s):
    if sum > n:
        return
    if sum == n:
        s = s.strip()
        res.append(s)
        return
    for j in range(i, 0, -1):
        Try(j, sum + j, s + str(j) + " ")

for i in range(int(input())):
    n = int(input())
    Try(n, 0, "")
    print(len(res))
    for i in res:
        print('(' + i + ')', end=' ')
    res.clear()
    print()