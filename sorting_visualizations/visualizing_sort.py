from p5 import *
from sorts import *
import random
import sys

heights = []
thick = 10

sorter = None
sort = bubble_sort
status = "doing"


def setup():
    global heights, sorter
    size(500, 500)
    heights = [random.randint(50, height - height // 10) for _ in range(width // (2 * thick))]
    sorter = sort(heights)


def draw():
    global status
    background(0, 0, 0)
    stroke(255, 50, 0)
    fill(255, 0, 0)

    if status == "doing":
        status, colors = next(sorter)
        print(status)
    else:
        colors = None
        input("Press any key to exit")
        sys.exit()

    for i in range(len(heights)):
        if colors and i in colors:
            stroke(*colors[i])
            fill(*colors[i])
        else:
            stroke(*RED)
            fill(*RED)
        rect((2 * i * thick, height - heights[i]), thick, heights[i])


def mouse_pressed():
    no_loop()


def mouse_released():
    loop()


if __name__ == '__main__':
    run(frame_rate=10)