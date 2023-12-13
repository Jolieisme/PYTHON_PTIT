from itertools import permutations

def list_permutations(iterable):
    return list(permutations(iterable))

t = int(input())
while t:
    a = []
    b = []
    num = int(input())
    for i in range(1, num+1):
        a.append(i)

    all_permutations = list_permutations(a)
    for i in all_permutations:
        x = ""
        for j in i:
            x += str(j)
        b.append(x)

    print(len(b))
    b.sort(reverse=True)
    for x in b:
        print(x, end=" ")
    print()
    t -= 1