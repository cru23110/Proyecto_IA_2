# Maze Pathfinding Algorithms

Implementation of maze generation and pathfinding algorithms for AI course project.

## Structure

```
.
├── src/
│   ├── algorithms/
│   │   ├── generation.py
│   │   └── pathfinding.py
│   ├── core/
│   │   └── maze.py
│   ├── visualization/
│   │   └── renderer.py
│   └── utils/
│       └── helpers.py
├── problem1.py
├── problem2.py
├── problem3.py
├── main.py
└── requirements.txt
```

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running

Interactive menu:
```bash
python main.py
```

Or run individual problems:
```bash
python problem1.py  # Maze generation (Kruskal vs Prim)
python problem2.py  # Solve 60x80 maze (BFS and A*)
python problem3.py  # Compare algorithms on 25 mazes
```

## Implementation

**Problem 1:** Generates mazes using Kruskal's and Prim's algorithms with step-by-step visualization.

**Problem 2:** Finds shortest path in a 60x80 maze from (0,0) to (59,79) using BFS and A*.

**Problem 3:** Runs BFS, DFS, Dijkstra, and A* on 25 random 45x55 mazes, comparing explored nodes, path length, and execution time.

## Requirements

- Python 3.9+
- pygame 2.5+
- numpy 1.24+
