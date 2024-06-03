from engine.app import *
from engine.storage import *
from engine.components import *

from dataclasses import dataclass

position = construct.component()
velocity = construct.component()
stamina = construct.component()
health = construct.component()

(construct.spec("player")
    (position, Vector2, 0, 0)
    (velocity, Vector2, 10, 8)
    (stamina, Scalar, 100)
    (health, Scalar, 2000))

(construct.spec("enemy")
    (position, Vector2, 0, 0)
    (velocity, Vector2, 5, 9)
    (health, Scalar, 1000))

p1 = construct.build("player")
for i in range(30000):
    construct.build("enemy")

    
async def movement_system():
    results = query.components(
        position,
        velocity)
    for pos, vel in results:
        pos.x += vel.x
        pos.y += vel.y

async def display_system():
    results = query.component(position)
    for pos in results:
        print(pos)

events = schedule.create()
update = schedule.create()
render = schedule.create()
loop   = schedule.create()

(schedule.register
    (update, movement_system)
    (render, display_system)

    (loop, schedule.phase, events)
    (loop, schedule.phase, update)
    (loop, schedule.phase, render))


def main():
    schedule.run(schedule.pipeline(loop))

if __name__ == "__main__":
    import timeit
    timeit.timeit('main()', number=5)

