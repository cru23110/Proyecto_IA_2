import pygame
import time


class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DARK_GRAY = (35, 35, 35)
    BLUE = (30, 144, 255)
    GREEN = (0, 200, 80)
    RED = (220, 50, 50)
    YELLOW = (255, 220, 0)
    ORANGE = (255, 140, 0)
    BG_DARK = (20, 20, 20)


class MazeRenderer:
    def __init__(self, maze, cell_size=12, title="Maze Visualization"):
        self.maze = maze
        self.cell_size = cell_size

        pygame.init()
        width = maze.cols * cell_size
        height = maze.rows * cell_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.font = pygame.font.SysFont("monospace", 14)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

    def draw_cell(self, row, col, color):
        cs = self.cell_size
        rect = pygame.Rect(col * cs + 1, row * cs + 1, cs - 1, cs - 1)
        pygame.draw.rect(self.screen, color, rect)

    def draw_maze_structure(self):
        cs = self.cell_size
        self.screen.fill(Colors.BLACK)

        for row in range(self.maze.rows):
            for col in range(self.maze.cols):
                pygame.draw.rect(
                    self.screen,
                    Colors.WHITE,
                    pygame.Rect(col * cs + 1, row * cs + 1, cs - 1, cs - 1)
                )

                passages = self.maze.cells[row][col]
                if 'S' in passages and row + 1 < self.maze.rows:
                    pygame.draw.rect(
                        self.screen,
                        Colors.WHITE,
                        pygame.Rect(col * cs + 1, (row + 1) * cs, cs - 1, 1)
                    )
                if 'E' in passages and col + 1 < self.maze.cols:
                    pygame.draw.rect(
                        self.screen,
                        Colors.WHITE,
                        pygame.Rect((col + 1) * cs, row * cs + 1, 1, cs - 1)
                    )

    def carve_passage(self, row1, col1, row2, col2, color=Colors.WHITE):
        cs = self.cell_size

        pygame.draw.rect(
            self.screen,
            color,
            pygame.Rect(col1 * cs + 1, row1 * cs + 1, cs - 1, cs - 1)
        )
        pygame.draw.rect(
            self.screen,
            color,
            pygame.Rect(col2 * cs + 1, row2 * cs + 1, cs - 1, cs - 1)
        )

        if row2 == row1 + 1:
            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect(col1 * cs + 1, (row1 + 1) * cs, cs - 1, 1)
            )
        elif row2 == row1 - 1:
            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect(col2 * cs + 1, (row2 + 1) * cs, cs - 1, 1)
            )
        elif col2 == col1 + 1:
            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect((col1 + 1) * cs, row1 * cs + 1, 1, cs - 1)
            )
        else:
            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect((col2 + 1) * cs, row2 * cs + 1, 1, cs - 1)
            )

    def animate_maze_generation(self, steps, delay=0.002, title="Generating Maze"):
        pygame.display.set_caption(title)
        cs = self.cell_size

        self.screen.fill(Colors.BLACK)
        for row in range(self.maze.rows):
            for col in range(self.maze.cols):
                pygame.draw.rect(
                    self.screen,
                    Colors.DARK_GRAY,
                    pygame.Rect(col * cs + 1, row * cs + 1, cs - 1, cs - 1)
                )
        pygame.display.flip()

        previous_edge = None

        for r1, c1, r2, c2 in steps:
            self.handle_events()

            if previous_edge:
                self.carve_passage(*previous_edge, color=Colors.WHITE)

            self.carve_passage(r1, c1, r2, c2, color=Colors.ORANGE)
            self.draw_cell(r1, c1, Colors.YELLOW)

            previous_edge = (r1, c1, r2, c2)
            pygame.display.flip()
            time.sleep(delay)

        if previous_edge:
            self.carve_passage(*previous_edge, color=Colors.WHITE)

        self.draw_cell(0, 0, Colors.GREEN)
        self.draw_cell(self.maze.rows - 1, self.maze.cols - 1, Colors.RED)
        pygame.display.flip()
        self.wait_for_key("Generation complete — press any key")

    def animate_pathfinding(self, explored, path, start, goal, delay=0.005, title="Pathfinding"):
        pygame.display.set_caption(title)
        self.draw_maze_structure()
        self.draw_cell(*start, Colors.GREEN)
        self.draw_cell(*goal, Colors.RED)
        pygame.display.flip()

        for node in explored:
            self.handle_events()
            if node != start and node != goal:
                self.draw_cell(*node, Colors.BLUE)
            pygame.display.flip()
            time.sleep(delay)

        if path:
            for node in path:
                self.handle_events()
                if node != start and node != goal:
                    self.draw_cell(*node, Colors.YELLOW)
                pygame.display.flip()
                time.sleep(delay * 2)

        path_length = len(path) if path else 0
        stats = f"Path: {path_length}  Explored: {len(explored)}"
        pygame.display.set_caption(f"{title} | {stats}")
        self.wait_for_key(f"{stats} — press any key")

    def draw_maze_at_offset(self, offset_x, offset_y, cs=None):
        if cs is None:
            cs = self.cell_size

        for row in range(self.maze.rows):
            for col in range(self.maze.cols):
                pygame.draw.rect(
                    self.screen,
                    Colors.WHITE,
                    pygame.Rect(offset_x + col * cs + 1, offset_y + row * cs + 1, cs - 1, cs - 1)
                )

                passages = self.maze.cells[row][col]
                if 'S' in passages and row + 1 < self.maze.rows:
                    pygame.draw.rect(
                        self.screen,
                        Colors.WHITE,
                        pygame.Rect(offset_x + col * cs + 1, offset_y + (row + 1) * cs, cs - 1, 1)
                    )
                if 'E' in passages and col + 1 < self.maze.cols:
                    pygame.draw.rect(
                        self.screen,
                        Colors.WHITE,
                        pygame.Rect(offset_x + (col + 1) * cs, offset_y + row * cs + 1, 1, cs - 1)
                    )

    def display_comparison(self, algorithms_results, start, goal):
        label_height = 18
        gap = 4
        title_bar = 40

        display_info = pygame.display.Info()
        usable_width = int(display_info.current_w * 0.82)
        usable_height = int(display_info.current_h * 0.82)

        max_cell_width = (usable_width - gap * 3) // 2
        max_cell_height = (usable_height - gap * 3 - title_bar - label_height * 2) // 2

        cs = min(max_cell_width // self.maze.cols, max_cell_height // self.maze.rows)
        cs = max(cs, 4)

        maze_width = self.maze.cols * cs
        maze_height = self.maze.rows * cs

        window_width = maze_width * 2 + gap * 3
        window_height = (maze_height + label_height) * 2 + gap * 3

        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Algorithm Comparison")
        self.screen.fill(Colors.BG_DARK)

        grid_positions = [
            (gap, gap),
            (gap * 2 + maze_width, gap),
            (gap, gap * 2 + maze_height + label_height),
            (gap * 2 + maze_width, gap * 2 + maze_height + label_height),
        ]

        start_row, start_col = start
        goal_row, goal_col = goal

        for idx, (algorithm_name, explored, path) in enumerate(algorithms_results):
            offset_x, offset_y = grid_positions[idx]

            self.draw_maze_at_offset(offset_x, offset_y, cs=cs)

            for row, col in explored:
                if (row, col) != start and (row, col) != goal:
                    pygame.draw.rect(
                        self.screen,
                        Colors.BLUE,
                        pygame.Rect(offset_x + col * cs + 1, offset_y + row * cs + 1, cs - 1, cs - 1)
                    )

            if path:
                for row, col in path:
                    if (row, col) != start and (row, col) != goal:
                        pygame.draw.rect(
                            self.screen,
                            Colors.YELLOW,
                            pygame.Rect(offset_x + col * cs + 1, offset_y + row * cs + 1, cs - 1, cs - 1)
                        )

            pygame.draw.rect(
                self.screen,
                Colors.GREEN,
                pygame.Rect(offset_x + start_col * cs + 1, offset_y + start_row * cs + 1, cs - 1, cs - 1)
            )
            pygame.draw.rect(
                self.screen,
                Colors.RED,
                pygame.Rect(offset_x + goal_col * cs + 1, offset_y + goal_row * cs + 1, cs - 1, cs - 1)
            )

            path_length = len(path) if path else 0
            label_text = f"{algorithm_name}  path:{path_length}  exp:{len(explored)}"
            text_surface = self.font.render(label_text, True, Colors.WHITE)
            self.screen.blit(text_surface, (offset_x + 2, offset_y + maze_height + 3))

        pygame.display.flip()
        self.wait_for_key("Press any key to continue")

    def wait_for_key(self, caption="Press any key"):
        pygame.display.set_caption(caption)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    return
            self.clock.tick(30)

    def close(self):
        pygame.quit()
