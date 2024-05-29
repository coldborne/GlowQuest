class Block:
    def __init__(self, num_directions=4):
        self.num_directions = num_directions
        self.connections = [False] * num_directions

    def switch_connection(self, direction):
        if 0 <= direction < self.num_directions:
            self.connections[direction] = not self.connections[direction]

    def is_connected(self, other_block):
        for direction in range(self.num_directions):
            opposite_direction = (direction + self.num_directions // 2) % self.num_directions

            if self.connections[direction] and other_block.connections[opposite_direction]:
                return True
        return False

    def get_connections(self):
        return self.connections.copy()

    def rotate(self, steps=1):
        steps = steps % self.num_directions
        self.connections = self.connections[-steps:] + self.connections[:-steps]
