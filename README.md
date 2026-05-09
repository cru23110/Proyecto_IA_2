# Maze Algorithms Project

Advanced implementation of maze generation and pathfinding algorithms for AI course.

## Project Structure

```
proyecto/
├── src/
│   ├── algorithms/
│   │   ├── generation.py      # Kruskal & Prim algorithms
│   │   └── pathfinding.py     # BFS, DFS, UCS, A*
│   ├── core/
│   │   └── maze.py            # Maze data structure
│   ├── visualization/
│   │   └── renderer.py        # Pygame-based visualization
│   └── utils/
│       └── helpers.py         # Shared utilities
├── problem1.py                # Maze generation comparison
├── problem2.py                # 60x80 maze solving
├── problem3.py                # Algorithm performance comparison
├── main.py                    # Interactive menu
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode
```bash
python main.py
```

### Direct Execution
```bash
python problem1.py
python problem2.py
python problem3.py
```

## Problems

### Problem 1: Maze Generation
Compares Kruskal's and Prim's algorithms for random maze generation with animated visualization.

### Problem 2: Maze Solving
Solves a 60x80 maze using BFS and A* algorithms, showing explored nodes and optimal path.

### Problem 3: Algorithm Comparison
Evaluates BFS, DFS, Dijkstra, and A* across 25 random 45x55 mazes with statistical analysis.

## Features

- Clean, modular architecture
- Animated visualizations
- Performance metrics
- Statistical comparison tables
- Professional code structure
