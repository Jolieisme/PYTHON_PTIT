def findIdx(n):
    for i in range(1, len(n)):
        if n[i-1] == n[i]:
            return -1
        if n[i] < n[i-1]:
            return i
    return -1

def check(n):
    if len(n) < 3:
        return "NO"
    
    idx = findIdx(n)

    if idx == -1:
        return "NO"
    
    for i in range(idx + 1, len(n)):
        if n[i] > n[i-1]:
            return "NO"
    return "YES"

test = int(input())
while test: 
    n = input()
    result = check(n)
    print(result)
    test -= 1
    
        
    
    
    
    