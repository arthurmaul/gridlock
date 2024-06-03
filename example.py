from engine.storage import (
    construct,
    deconstruct,
    command,
    query)

from dataclasses import dataclass

@dataclass(slots=True)
class Vector2:
    x: int
    y: int

@dataclass(slots=True)
class Scalar:
    value: int

(position,
velocity,
stamina,
health
) = construct.components(4)

(construct.spec("player")
    (position, Vector2, 0, 0)
    (velocity, Vector2, 0, 0)
    (stamina, Scalar, 100)
    (health, Scalar, 2000))

(construct.spec("enemy")
    (position, Vector2, 0, 0)
    (velocity, Vector2, 0, 0)
    (health, Scalar, 1000))

p1 = construct.build("player")
e1 = construct.build("enemy")
    
print(query.table)
results = query.components(
    position,
    velocity,
    stamina)
for p, v, s in results:
    print(p, v, s)

print(*query.component(health))
print(*query.entity(p1))
