import sys
import time
import random
sys.path.insert(0, '.')

from src.algorithms import (
    kruskal_algorithm,
    prim_algorithm,
    breadth_first_search,
    depth_first_search,
    uniform_cost_search,
    a_star_search
)
from src.visualization import MazeRenderer


GRID_ROWS = 45
GRID_COLS = 55
CELL_SIZE = 8
NUM_MAZES = 25
MIN_MANHATTAN_DISTANCE = 10


ALGORITHMS = [
    ("BFS", breadth_first_search),
    ("DFS", depth_first_search),
    ("Dijkstra", uniform_cost_search),
    ("A*", a_star_search),
]


def generate_random_positions(rows, cols, rng):
    while True:
        start_row = rng.randint(0, rows - 1)
        start_col = rng.randint(0, cols - 1)
        goal_row = rng.randint(0, rows - 1)
        goal_col = rng.randint(0, cols - 1)

        manhattan = abs(start_row - goal_row) + abs(start_col - goal_col)
        if manhattan >= MIN_MANHATTAN_DISTANCE:
            return (start_row, start_col), (goal_row, goal_col)


def main():
    print("=" * 70)
    print("Problem 3: Algorithm Comparison — 25 Random Mazes")
    print("=" * 70)

    rng = random.Random(2026)

    total_nodes_explored = {name: 0 for name, _ in ALGORITHMS}
    total_path_length = {name: 0 for name, _ in ALGORITHMS}
    total_execution_time = {name: 0.0 for name, _ in ALGORITHMS}
    total_ranking = {name: 0 for name, _ in ALGORITHMS}

    header = f"{'#':>3} | {'Algorithm':<10} | {'Explored':>9} | {'Path':>6} | {'Time(ms)':>9} | {'Rank':>4}"
    separator = "-" * len(header)

    for maze_idx in range(NUM_MAZES):
        generator = kruskal_algorithm if maze_idx % 2 == 0 else prim_algorithm
        maze, _ = generator(GRID_ROWS, GRID_COLS, seed=maze_idx * 13)

        start_pos, goal_pos = generate_random_positions(GRID_ROWS, GRID_COLS, rng)

        generator_name = "Kruskal" if maze_idx % 2 == 0 else "Prim"
        print(f"\n{'='*70}")
        print(f"Maze {maze_idx + 1:>2}/{NUM_MAZES}  |  start={start_pos}  goal={goal_pos}  |  generator={generator_name}")
        print(separator)
        print(header)
        print(separator)

        maze_results = []

        for algorithm_name, algorithm_func in ALGORITHMS:
            start_time = time.perf_counter()
            path, explored = algorithm_func(maze, start_pos, goal_pos)
            elapsed_time_ms = (time.perf_counter() - start_time) * 1000

            path_length = len(path) if path else 0

            total_nodes_explored[algorithm_name] += len(explored)
            total_path_length[algorithm_name] += path_length
            total_execution_time[algorithm_name] += elapsed_time_ms

            maze_results.append((algorithm_name, explored, path, path_length, elapsed_time_ms))

        ranked_results = sorted(maze_results, key=lambda x: len(x[1]))

        for rank, (algorithm_name, explored, path, path_length, elapsed_time_ms) in enumerate(ranked_results, 1):
            total_ranking[algorithm_name] += rank
            print(f"{'':>3} | {algorithm_name:<10} | {len(explored):>9} | {path_length:>6} | {elapsed_time_ms:>9.2f} | {rank:>4}")

        if maze_idx < 3:
            renderer = MazeRenderer(maze, cell_size=CELL_SIZE)
            renderer.display_comparison(
                [(name, explored, path) for name, explored, path, _, _ in maze_results],
                start_pos,
                goal_pos
            )
            renderer.close()

    print(f"\n{'='*70}")
    print("SUMMARY TABLE — Average Performance Across 25 Mazes")
    print(f"{'='*70}")
    summary_header = f"{'Algorithm':<10} | {'Avg Explored':>12} | {'Avg Path':>9} | {'Avg Time(ms)':>12} | {'Avg Rank':>9}"
    print(summary_header)
    print("-" * 70)

    for algorithm_name, _ in ALGORITHMS:
        avg_explored = total_nodes_explored[algorithm_name] / NUM_MAZES
        avg_path = total_path_length[algorithm_name] / NUM_MAZES
        avg_time = total_execution_time[algorithm_name] / NUM_MAZES
        avg_rank = total_ranking[algorithm_name] / NUM_MAZES

        print(f"{algorithm_name:<10} | {avg_explored:>12.1f} | {avg_path:>9.1f} | {avg_time:>12.3f} | {avg_rank:>9.2f}")

    print(f"{'='*70}")
    print("Problem 3 completed successfully!")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
