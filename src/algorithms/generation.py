import random
from src.core.maze import Maze


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


def kruskal_algorithm(rows, cols, seed=None):
    rng = random.Random(seed)
    maze = Maze(rows, cols)
    ds = DisjointSet(rows * cols)

    edges = []
    for r in range(rows):
        for c in range(cols):
            if c + 1 < cols:
                edges.append((r, c, r, c + 1, 'E'))
            if r + 1 < rows:
                edges.append((r, c, r + 1, c, 'S'))

    rng.shuffle(edges)
    construction_steps = []

    for r1, c1, r2, c2, direction in edges:
        cell1_id = r1 * cols + c1
        cell2_id = r2 * cols + c2

        if ds.union(cell1_id, cell2_id):
            maze.connect_cells(r1, c1, direction)
            construction_steps.append((r1, c1, r2, c2))

    return maze, construction_steps


def prim_algorithm(rows, cols, seed=None):
    rng = random.Random(seed)
    maze = Maze(rows, cols)

    start_row = rng.randint(0, rows - 1)
    start_col = rng.randint(0, cols - 1)

    visited = {(start_row, start_col)}
    frontier = []

    for next_row, next_col, direction in maze.get_all_neighbors(start_row, start_col):
        frontier.append((start_row, start_col, next_row, next_col, direction))

    construction_steps = []

    while frontier:
        idx = rng.randint(0, len(frontier) - 1)
        from_row, from_col, to_row, to_col, direction = frontier.pop(idx)

        if (to_row, to_col) in visited:
            continue

        maze.connect_cells(from_row, from_col, direction)
        construction_steps.append((from_row, from_col, to_row, to_col))
        visited.add((to_row, to_col))

        for next_row, next_col, next_dir in maze.get_all_neighbors(to_row, to_col):
            if (next_row, next_col) not in visited:
                frontier.append((to_row, to_col, next_row, next_col, next_dir))

    return maze, construction_steps
