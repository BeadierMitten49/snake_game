import tkinter as tk
from service import WindowService


class Window(tk.Tk):
    def __init__(self, grid_h, grid_w):
        super().__init__()

        self.grid_h = grid_h
        self.grid_w = grid_w

        self.window_service = WindowService(self.grid_h, self.grid_w)

        w = 400
        h = 400

        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.title('Snake game')

        self.grid_frame = GridFrame(self)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.bind("<Up>", self.move_up)
        self.bind("<Down>", self.move_down)
        self.bind("<Right>", self.move_right)
        self.bind("<Left>", self.move_left)

        self.bind("<space>", self.create_food)

    def move_up(self, event):
        self.window_service.snake_head.move_up()
        self.update_snake()

    def move_down(self, event):
        self.window_service.snake_head.move_down()
        self.update_snake()

    def move_right(self, event):
        self.window_service.snake_head.move_right()
        self.update_snake()

    def move_left(self, event):
        self.window_service.snake_head.move_left()
        self.update_snake()

    def update_snake(self):
        self.window_service.move()
        self.window_service.food_eaten()
        self.grid_frame.update_grid()

    def create_food(self, event):
        self.window_service.create_food()
        self.grid_frame.update_grid()


class GridFrame(tk.Frame):
    def __init__(self, parent: Window):
        super().__init__(parent, bg="blue")
        self.parent = parent
        self.labels = []

        for row in range(self.parent.grid_h):
            self.rowconfigure(row, weight=1)
            rows_arr = []
            for col in range(self.parent.grid_w):
                self.columnconfigure(col, weight=1)
                label = tk.Label(self, text=f"0", width=1, height=1)
                label.grid(row=row, column=col, padx=1, pady=1, sticky=tk.NSEW)
                rows_arr.append(label)
            self.labels.append(rows_arr)

    def update_grid(self):
        self.clear()
        for x, y in self.parent.window_service.snake:
            self.labels[y][x].configure(text="", bg="orange")

        f_x, f_y = self.parent.window_service.food_coordinates
        self.labels[f_y][f_x].configure(text="", bg="green")

    def clear(self):
        for rows in self.labels:
            for label in rows:
                label.config(text="", bg="white")
