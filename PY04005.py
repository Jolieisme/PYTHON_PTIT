from math import *
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        AB = sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
        AC = sqrt((x3-x1) ** 2 + (y3-y1) ** 2)
        BC = sqrt((x3-x2) ** 2 + (y3-y2) ** 2)
        