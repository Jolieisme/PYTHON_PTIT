n = input()
use = [0] * 15

def Try(s):
    if len(s) == len(n):
        print(s)
        return
    for i in range(len(n)):
        if use[i] == 0:
            use[i] = 1
            Try(s + n[i])
            use[i] = 0

Try("")