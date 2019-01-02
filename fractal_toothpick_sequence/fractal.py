# https://www.youtube.com/watch?v=-OL_sw2MiYw&t=651s

from toothpick import ToothPick
from collections import defaultdict
from p5 import *

toothpicks = []
points = defaultdict(int)
factor = 1


def setup():
    size(1080, 1080)
    initial = ToothPick(0, 0, ishorizontal=True)
    toothpicks.append(initial)
    points[initial.v1] += 1
    points[initial.v2] += 1
    no_loop()


def mouse_pressed():
    no_loop()


def mouse_released():
    loop()


def draw():
    print(len(toothpicks))
    global factor
    background(255)
    next_gen = []
    translate(width / 2, height / 2)
    scale(factor)
    minx = min(toothpicks, key=lambda x: min(x.x1, x.x2))
    maxx = max(toothpicks, key=lambda x: max(x.x1, x.x2))
    minx = min(minx.x1, minx.x2)
    maxx = max(maxx.x1, maxx.x2)

    factor = width / (200 + maxx - minx)

    for toothpick in toothpicks:
        toothpick.show()

        if toothpick.new:
            if points[toothpick.v1] == 1:
                next_gen.append(
                    ToothPick(*toothpick.v1, not toothpick.ishorizontal)
                )

            if points[toothpick.v2] == 1:
                next_gen.append(
                    ToothPick(*toothpick.v2, not toothpick.ishorizontal)
                )
            toothpick.new = False

    for each in next_gen:
        points[each.v1] += 1
        points[each.v2] += 1

    toothpicks.extend(next_gen)


if __name__ == '__main__':
    run(frame_rate=10)
