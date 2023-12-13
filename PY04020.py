class Bill:
    def __init__(self, id, name, sl, dongia, chietkhau):
        self.id = id
        self.name = name
        self.sl = sl
        self.chietkhau = chietkhau
        self.dongia = dongia
        self.total = self.dongia * self.sl - self.chietkhau

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.name, self.sl, self.dongia, self.chietkhau, self.total)


a = []
t = int(input())
for i in range(t):
    x = Bill(input(), input(), int(input()), int(input()), int(input()))
    a.append(x)

a.sort(key=lambda x: -x.total)
for i in a:
    print(i)