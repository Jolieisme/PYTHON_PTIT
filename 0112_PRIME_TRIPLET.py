test = int(input())
prime = [1] * 1000005
prime[0] = prime[1] = 0
for i in range(1000):
    if prime[i]:
        for j in range(i * i, 1000000, i):
            prime[j] = 0

while test:
    cnt = 0
    n = int(input())
    for i in range(n-6):
        if prime[i] and prime[i + 6]:
            if prime[i + 2] or prime[i + 4]:
                cnt += 1
    print(cnt)
    test -= 1
