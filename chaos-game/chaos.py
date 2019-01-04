from p5 import *
import random

num_seed_points = 4
seed_points = []
current = None

colors = [
    (245, 130, 48),
    (145, 30, 180),
    (230, 25, 75),
    (60, 180, 75),
    (255, 225, 25),
    (0, 130, 200),
    (240, 50, 230),
    (210, 245, 60),
    (250, 190, 190),
    (0, 128, 128),
    (230, 190, 255),
    (170, 110, 40),
    (255, 250, 200),
    (128, 0, 0),
    (170, 255, 195),
    (128, 128, 0),
    (255, 215, 180),
    (0, 0, 128),
    (128, 128, 128),
    (255, 255, 255),
]


def setup():
    # size(500, 500)
    r = width / 2 - 10
    for i in range(num_seed_points):
        angle = i * TWO_PI / num_seed_points
        seed_points.append(Vector(r * cos(angle), r * sin(angle)))
    global current
    current = Vector(random_uniform(r), random_uniform(r))
    background(0)


def draw():
    size = 1
    translate(width / 2, height / 2)
    rotate(PI / num_seed_points)

    stroke(255)
    fill(255)
    for each in seed_points:
        circle(each, size * 3)

    for i in range(100):
        toss = random.randint(0, num_seed_points - 1)
        color = colors[(toss) % len(colors)]
        stroke(*color)
        fill(*color)
        global current
        current = current.lerp(seed_points[toss], 0.5)
        circle(current, size)

    # save_frame()


if __name__ == '__main__':
    run()
