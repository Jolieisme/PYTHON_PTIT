n = int(input())
a = []
result = []
while len(a) < n:
    a.extend(list(map(int, input().split())))

MAX = max(a)

for i in range(1, MAX):
    if i not in a:
        result.append(i)

if len(result) == 0:
    print("Excellent!")
else:
    for i in result:
        print(i)