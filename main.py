import random
import tkinter as tk
from tkinter import simpledialog
from block import StraightBlock, CornerBlock


class GameBoard:
    def __init__(self, size, start_x, start_y):
        self.size = size
        self.grid = self.__create_game_field(self.size, self.size)
        self.start_position = (start_x, start_y)
        self.__update_connections(start_x, start_y)

    def rotate_block(self, x, y, steps=1):
        if not (0 <= x < len(self.grid) and 0 <= y < len(self.grid[x])):
            raise IndexError("x or y is out of bounds")

        self.grid[x][y].rotate(steps)
        self.__update_connections(self.start_position[0], self.start_position[1])

    def __create_game_field(self, width, height):
        blocks = []

        for _ in range(width):
            row = []

            for _ in range(height):
                if random.randint(0, 1) == 0:
                    row.append(StraightBlock())
                else:
                    row.append(CornerBlock())

            blocks.append(row)

        return blocks

    def __update_connections(self, start_x, start_y):
        for row in self.grid:
            for block in row:
                block.is_highlighted = False

        self.grid[start_x][start_y].enable_connection()

        visited = set()
        queue = [(start_x, start_y)]

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            x, y = queue.pop(0)

            if (x, y) not in visited:
                visited.add((x, y))
                current_block = self.grid[x][y]

                for direction, (dx, dy) in enumerate(directions):
                    if current_block.sides[direction]:
                        next_x, next_y = x + dx, y + dy

                        if 0 <= next_x < self.size and 0 <= next_y < self.size:
                            neighbor = self.grid[next_x][next_y]

                            if current_block.is_connected(neighbor, direction):
                                if not neighbor.is_highlighted:
                                    neighbor.enable_connection()
                                    queue.append((next_x, next_y))


# Графический интерфейс с использованием Tkinter
class LightEmUpGame:
    def __init__(self, root):
        self.root = root
        self.size = self.get_size()
        self.board = GameBoard(self.size, 0, 0, [0, 1, 0, 0])
        self.time_left = 10  # Время на игру в секундах
        self.timer_label = None
        self.game_over = False
        self.create_widgets()
        self.update_ui()
        self.update_timer()

    def get_size(self):
        size = 0
        while size < 10 or size > 100:
            size = simpledialog.askinteger("Field Size", "Enter size of the field (10-100):", minvalue=10, maxvalue=100)
            if size is None:  # Если пользователь закрыл диалоговое окно
                size = 10
        return size

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.size * 50, height=self.size * 50)
        self.canvas.pack()

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}")
        self.timer_label.pack()

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_button.pack()

    def update_ui(self):
        self.canvas.delete("all")
        for i in range(self.size):
            for j in range(self.size):
                block = self.board.grid[i][j]
                x1, y1 = j * 50, i * 50
                x2, y2 = x1 + 50, y1 + 50
                color = "yellow" if any(block.connections) else "grey"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=self.get_block_symbol(block))
        if self.check_win() and not self.game_over:
            self.game_over = True
            self.show_message("You win!")
        self.root.after(100, self.update_ui)

    def get_block_symbol(self, block):
        connections = block.get_connections()
        if connections == [True, True, False, False]:
            return "┃"
        elif connections == [False, False, True, True]:
            return "━"
        elif connections == [True, False, True, False]:
            return "┓"
        elif connections == [True, False, False, True]:
            return "┛"
        elif connections == [False, True, True, False]:
            return "┏"
        elif connections == [False, True, False, True]:
            return "┗"
        else:
            return " "

    def rotate_block(self, event):
        if not self.game_over:
            x, y = event.x // 50, event.y // 50
            if 0 <= x < self.size and 0 <= y < self.size:
                self.board.rotate_block(y, x)
                self.update_ui()

    def restart(self):
        self.size = self.get_size()
        self.board = GameBoard(self.size)
        self.time_left = 120
        self.game_over = False
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.update_ui()
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0 and not self.game_over:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and not self.game_over:
            self.game_over = True
            self.show_message("Time's up!")

    def check_win(self):
        for row in self.board.grid:
            for block in row:
                if not any(block.connections):
                    return False
        return True

    def show_message(self, message):
        msg_box = tk.Toplevel()
        msg_box.title("Game Over")
        tk.Label(msg_box, text=message).pack()
        tk.Button(msg_box, text="OK", command=msg_box.destroy).pack()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            if not self.game_over:
                self.game_over = True
                self.show_message("Time's up!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Light'em Up!")
    game = LightEmUpGame(root)
    root.bind("<Button-1>", game.rotate_block)
    root.mainloop()
