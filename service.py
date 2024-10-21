import random

def create_grid(grid_h, grid_w):
    grid = [[0 for _ in range(grid_w)] for _ in range(grid_h)]
    return grid


class WindowService:
    def __init__(self, grid_h, grid_w):
        self.grid_h = grid_h
        self.grid_w = grid_w

        self.snake = []
        self.snake_head = Head(self.grid_h, self.grid_w)

        self.snake_len = 5

        self.food_coordinates = ()

    def move(self):
        self.add_snake()
        if len(self.snake) > self.snake_len:
            self.remove_snake()

    def add_snake(self):
        self.snake.append((self.snake_head.x, self.snake_head.y))

    def remove_snake(self):
        self.snake.pop(0)

    def create_food(self):
        x = random.randint(0, self.grid_w - 1)
        y = random.randint(0, self.grid_h - 1)

        if (x, y) in self.snake:
            self.create_food()
        else:
            self.food_coordinates = (x, y)

    def food_eaten(self):
        if self.snake[-1] == self.food_coordinates:
            self.snake_len += 1
            self.create_food()


class Head:
    x = 0
    y = 0

    def __init__(self, grid_h, grid_w):
        self.grid_h = grid_h
        self.grid_w = grid_w

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def __str__(self):
        return 1
