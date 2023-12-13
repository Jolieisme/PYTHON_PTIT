n, m = map(int, input().split())
tmp = n
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(tmp):
    if n > m:
        if i % 2 == 0:
            a.remove(a[i])
            a.insert(0, i)
            n -= 1
    elif n == m:
        break

for x in a:
    if x == 0:
        a.remove(x)

for i in a:
    print(i)




'''
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''

''' 
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9
'''
