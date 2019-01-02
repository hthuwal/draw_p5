from p5 import *
from particle import Particle
import random
current = None
particles = []


def setup():
    size(500, 500)
    rotate(PI / 6)
    global current
    current = Particle(width / 2, 0)


def draw():
    global current
    translate(width / 2, height / 2)
    background(0)

    while not current.finished() and not current.intersects(particles):
        current.update()

    particles.append(current)
    current = Particle(width / 2, random.randint(0, 10))

    for i in range(6):
        rotate(PI / 3)
        current.show()
        for p in particles:
            p.show()

        with push_matrix():
            scale(1, -1)
            current.show()
            for p in particles:
                p.show()

    # save_frame()


if __name__ == '__main__':
    run()
