m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res1 = []
res2 = []
res3 = []
for i in a:
    if i in b:
        res1.append(i)
    else:
        res2.append(i)

for i in b:
    if i not in a:
        res3.append(i)

res1.sort()
res2.sort()
res3.sort()
for i in res1:
    print(i, end=" ")
print()
for i in res2:
    print(i, end=" ")
print()
for i in res3:
    print(i, end=" ")


