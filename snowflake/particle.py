from p5 import *
import random


class Particle:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.r = 3

    def update(self):
        self.pos.x -= 1
        self.pos.y += random.randint(-3, 3)

        angle = self.pos.angle
        angle = constrain(angle, 0, PI / 6)
        self.pos.angle = angle

    def show(self):
        fill(255)
        stroke(255)
        circle((self.pos.x, self.pos.y), self.r)

    def finished(self):
        return self.pos.x < 1

    def intersects(self, particles):
        for p in particles:
            d = distance((self.pos.x, self.pos.y), (p.pos.x, p.pos.y))
            if d <= 2 * self.r:
                # print(d, self.r)
                return True
                break
        return False
