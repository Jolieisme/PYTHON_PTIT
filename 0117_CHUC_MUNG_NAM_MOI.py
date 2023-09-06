test = int(input())
dict = {}

while test:
    s = input()
    dict[s] = 1
    test -= 1
print(len(dict))