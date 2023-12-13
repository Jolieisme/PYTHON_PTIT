class GV:
    def __init__(self, id, name, ma_xt, tin_hoc, chuyen_mon):
        self.id = "GV{:02d}".format(id)
        self.name = name
        self.ma_xt = ma_xt
        if self.ma_xt[0] == 'A':
            self.mon = "TOAN"
        elif self.ma_xt[0] == 'B':
            self.mon = "LY"
        else:
            self.mon = "HOA"

        if self.ma_xt[1] == '1':
            self.ut = 2.0
        elif self.ma_xt[1] == '2':
            self.ut = 1.5
        elif self.ma_xt[1] == '3':
            self.ut = 1.0
        else:
            self.ut = 0.0

        self.tin_hoc = tin_hoc
        self.chuyen_mon = chuyen_mon
        self.total = self.tin_hoc * 2 + self.chuyen_mon + self.ut
        if self.total >= 18:
            self.kq = "TRUNG TUYEN"
        else:
            self.kq = "LOAI"

    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.id, self.name, self.mon, round(self.total, 2), self.kq)

def cmp(a):
    return (a.total, (-1) * a.id)


LIST = []
t = int(input())
for i in range(t):
    x = GV(i+1, input(), input(), float(input()), float(input()))
    LIST.append(x)

LIST.sort(key=cmp, reverse=True)

for i in LIST:
    print(i)

