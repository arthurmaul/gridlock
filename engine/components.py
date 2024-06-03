from dataclasses import dataclass, field

@dataclass(slots=True)
class Scalar:
    value: int | str = 0

@dataclass(slots=True)
class Vector2:
    x: float = 0
    y: float = 0

@dataclass
class Transform2D:
    position: Vector2 = field(default_factory=Vector2)
    dimension: Vector2 = field(default_factory=Vector2)
    scale: Vector2 = field(default_factory=Vector2)

