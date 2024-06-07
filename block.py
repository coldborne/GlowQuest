class Block:
    def __init__(self, num_directions=4):
        self.num_directions = num_directions
        self.sides = [False] * num_directions
        self.is_highlighted = False

    def enable_connection(self):
        self.is_highlighted = True

    def disable_connection(self):
        self.is_highlighted = False

    def is_connected(self, other_block, direction):
        side = self.sides[direction]
        opposite_side_index = (direction + self.num_directions // 2) % self.num_directions
        opposite_side = other_block.get_sides()[opposite_side_index]

        return side and opposite_side

    def rotate(self, steps=1):
        steps = steps % self.num_directions
        self.sides = self.sides[-steps:] + self.sides[:-steps]

    def get_sides(self):
        return self.sides.copy()


class StraightBlock(Block):
    def __init__(self):
        super().__init__()
        self.sides = [True, False, True, False]


class CornerBlock(Block):
    def __init__(self):
        super().__init__()
        self.sides = [True, True, False, False]
