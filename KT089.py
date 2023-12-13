n = int(input())
a = list(map(int, input().split()))
chan = []
le = []
for i in a:
    if(i % 2 == 0):
        chan.append(i)
    else:
        le.append(i)
chan.sort(reverse= True)
le.sort()
for i in a:
    if(i % 2 == 0):
        print(chan[-1], end = " ")
        chan.pop()
    else:
        print(le[-1])
        le.pop()

