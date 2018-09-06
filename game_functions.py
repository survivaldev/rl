# import libtcodpy as libtcod
from game_data import Direction
import random


def random_int(a: int, b: int) -> int:
    if a > b:
        return random.randint(b, a)
    return random.randint(a, b)


def random_bool() -> bool:
    return bool(random.getrandbits(1))


def direction_to_str(direction: tuple) -> Direction:
    """(1, 1) = SE. In a 41*41 matrix it generates 200*4 diagonals, 220*4 others, 1 X"""
    direction_x, direction_y = direction
    if direction_x > 0:
        if 0.5 < direction_y/direction_x < 2.0:
            return Direction.SE
        elif -0.5 <= direction_y/direction_x <= 0.5:
            return Direction.E
    if direction_x < 0:
        if 0.5 < direction_y/direction_x < 2.0:
            return Direction.NW
        elif -0.5 <= direction_y/direction_x <= 0.5:
            return Direction.W
    if direction_y > 0:
        if -2.0 < direction_x/direction_y < -0.5:
            return Direction.SW
        elif -0.5 <= direction_x/direction_y <= 0.5:
            return Direction.S
    if direction_y < 0:
        if -2.0 < direction_x/direction_y < -0.5:
            return Direction.NE
        elif -0.5 <= direction_x/direction_y <= 0.5:
            return Direction.N
    return Direction.X
