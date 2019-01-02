from p5 import *


class ToothPick():
    length = 27

    def __init__(self, cx, cy, ishorizontal=False):
        self.ishorizontal = ishorizontal
        self.new = True
        # self.cx, self.cy = cx, cy
        if ishorizontal:
            self.x1 = cx - ToothPick.length // 2
            self.x2 = cx + ToothPick.length // 2
            self.y1 = cy
            self.y2 = cy
            # self.width = ToothPick.length
            # self.height = 3
        else:
            self.x1 = cx
            self.x2 = cx
            self.y1 = cy - ToothPick.length // 2
            self.y2 = cy + ToothPick.length // 2
            # self.width = 3
            # self.height = ToothPick.length

    @property
    def v1(self):
        return self.x1, self.y1

    @property
    def v2(self):
        return self.x2, self.y2

    def show(self):
        stroke(0)
        if self.new:
            stroke(0, 0, 255)
        fill(0)
        # rect((self.cx, self.cy), self.width, self.height, mode='CENTER')
        line((self.x1, self.y1), (self.x2, self.y2))
