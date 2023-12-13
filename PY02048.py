n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# 1 2 3 4 6 7 9
s = 1
for i in range(1, n):
    if a[i] - a[i-1] > k:
        s += 1

print(s)