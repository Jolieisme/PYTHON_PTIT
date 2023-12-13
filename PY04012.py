class Student:
    def __init__(self, id, name, lop):
        self.id = id
        self.name = name
        self.lop = lop
        self.p = 10

    def calc(self, s):
        for i in s:
            if i == 'm':
                self.p -= 1
            elif i == 'v':
                self.p -= 2
        if self.p <= 0:
            self.p = 0

    def prt(self):
        print(self.id + " " + self.name + " " + self.lop + " " + str(self.p), end='')
        if self.p == 0:
            print(" KDDK", end='')
        print()


m = {}
a = []
t = int(input())
t2 = t
while t:
    tmp = Student(input(), input(), input())
    m[tmp.id] = tmp
    a.append(tmp)
    t -= 1

while t2:
    id, status = input().split()
    m[id].calc(status)
    t2 -= 1
for i in a:
    i.prt()


'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
'''