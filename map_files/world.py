
# TODO all of this


class Tile:
    pass


class Floor:
    def __init__(self):
        self.map: list = []  # [[Tile() for _ in range(30)] for _ in range(30)]

    def is_inside_map(self, x: int, y: int) -> bool:
        return True


class Position:
    def __init__(self, x: int, y: int, floor: Floor):
        self.x: int = x
        self.y: int = y
        self.floor: Floor = floor

    def update(self, new_x: int, new_y: int, new_floor: Floor):
        self.x = new_x
        self.y = new_y
        self.floor = new_floor

    def get_tile(self) -> Tile:
        return self.floor.map[self.x][self.y]

    def is_inside_map(self) -> bool:
        return self.floor.is_inside_map(self.x, self.y)
