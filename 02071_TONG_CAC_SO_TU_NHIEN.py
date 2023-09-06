res = []
test = int(input())
def Try(i, sum, a):
    if sum > n:
        return
    if sum == n:
        a = a.strip()
        res.append(a)
        return
    for j in range(i, 0, -1):
        Try(j, sum + j, a + str(j) + " ")

while test:
    n = int(input())
    s = ""
    Try(n, 0, "")
    print(len(res))
    for i in res:
        print("(" + i + ") ", end = "")
    res.clear()
    print()
    test -= 1


    