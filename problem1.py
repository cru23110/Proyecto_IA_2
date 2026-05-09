import sys
sys.path.insert(0, '.')

from src.algorithms import kruskal_algorithm, prim_algorithm
from src.visualization import MazeRenderer


GRID_ROWS = 30
GRID_COLS = 40
CELL_SIZE = 18


def main():
    print("=" * 60)
    print("Problem 1: Maze Generation Algorithms")
    print("=" * 60)

    print("\n[1/2] Generating maze using Kruskal's algorithm...")
    maze_kruskal, steps_kruskal = kruskal_algorithm(GRID_ROWS, GRID_COLS, seed=42)
    renderer = MazeRenderer(maze_kruskal, cell_size=CELL_SIZE, title="Kruskal's Algorithm")
    renderer.animate_maze_generation(steps_kruskal, delay=0.003, title="Kruskal — Maze Generation")
    renderer.close()

    print("\n[2/2] Generating maze using Prim's algorithm...")
    maze_prim, steps_prim = prim_algorithm(GRID_ROWS, GRID_COLS, seed=42)
    renderer = MazeRenderer(maze_prim, cell_size=CELL_SIZE, title="Prim's Algorithm")
    renderer.animate_maze_generation(steps_prim, delay=0.003, title="Prim — Maze Generation")
    renderer.close()

    print("\n" + "=" * 60)
    print("Problem 1 completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
