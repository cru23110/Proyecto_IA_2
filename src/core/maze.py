import numpy as np


class Maze:
    DIRECTIONS = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }

    OPPOSITE = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[set() for _ in range(cols)] for _ in range(rows)]

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def connect_cells(self, row, col, direction):
        dr, dc = self.DIRECTIONS[direction]
        next_row, next_col = row + dr, col + dc

        if self.is_valid_position(next_row, next_col):
            self.cells[row][col].add(direction)
            self.cells[next_row][next_col].add(self.OPPOSITE[direction])

    def get_all_neighbors(self, row, col):
        neighbors = []
        for direction, (dr, dc) in self.DIRECTIONS.items():
            next_row, next_col = row + dr, col + dc
            if self.is_valid_position(next_row, next_col):
                neighbors.append((next_row, next_col, direction))
        return neighbors

    def get_connected_neighbors(self, row, col):
        neighbors = []
        for direction in self.cells[row][col]:
            dr, dc = self.DIRECTIONS[direction]
            neighbors.append((row + dr, col + dc))
        return neighbors

    def to_image_grid(self, cell_size=10):
        height = self.rows * cell_size + 1
        width = self.cols * cell_size + 1
        grid = np.ones((height, width), dtype=bool)

        for row in range(self.rows):
            for col in range(self.cols):
                top = row * cell_size + 1
                left = col * cell_size + 1
                grid[top:top+cell_size-1, left:left+cell_size-1] = False

                if 'S' in self.cells[row][col]:
                    grid[top+cell_size-1, left:left+cell_size-1] = False
                if 'E' in self.cells[row][col]:
                    grid[top:top+cell_size-1, left+cell_size-1] = False

        return grid
