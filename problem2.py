import sys
sys.path.insert(0, '.')

from src.algorithms import kruskal_algorithm, breadth_first_search, a_star_search
from src.visualization import MazeRenderer


GRID_ROWS = 60
GRID_COLS = 80
CELL_SIZE = 10
START_POSITION = (0, 0)
GOAL_POSITION = (GRID_ROWS - 1, GRID_COLS - 1)


def main():
    print("=" * 60)
    print("Problem 2: Solving 60x80 Maze")
    print("=" * 60)

    print("\nGenerating maze...")
    maze, _ = kruskal_algorithm(GRID_ROWS, GRID_COLS, seed=7)

    algorithms = [
        ("BFS", breadth_first_search),
        ("A*", a_star_search),
    ]

    for algorithm_name, algorithm_func in algorithms:
        print(f"\n[{algorithm_name}] Searching for path...")
        path, explored = algorithm_func(maze, START_POSITION, GOAL_POSITION)

        path_length = len(path) if path else 0
        print(f"  Nodes explored: {len(explored)}")
        print(f"  Path length: {path_length}")

        renderer = MazeRenderer(maze, cell_size=CELL_SIZE, title=algorithm_name)
        renderer.animate_pathfinding(
            explored,
            path,
            START_POSITION,
            GOAL_POSITION,
            delay=0.001,
            title=f"{algorithm_name} | explored:{len(explored)} path:{path_length}"
        )
        renderer.close()

    print("\n" + "=" * 60)
    print("Problem 2 completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
