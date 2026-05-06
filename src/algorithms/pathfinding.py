import heapq
from collections import deque
from src.utils.helpers import reconstruct_path, manhattan_distance


def breadth_first_search(maze, start, goal):
    queue = deque([start])
    parent = {start: None}
    explored = []

    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == goal:
            return reconstruct_path(parent, goal), explored

        for neighbor in maze.get_connected_neighbors(*current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return None, explored


def depth_first_search(maze, start, goal):
    stack = [start]
    parent = {start: None}
    explored = []

    while stack:
        current = stack.pop()
        explored.append(current)

        if current == goal:
            return reconstruct_path(parent, goal), explored

        for neighbor in maze.get_connected_neighbors(*current):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return None, explored


def uniform_cost_search(maze, start, goal):
    heap = [(0, start)]
    parent = {start: None}
    cost = {start: 0}
    explored = []

    while heap:
        current_cost, current = heapq.heappop(heap)
        explored.append(current)

        if current == goal:
            return reconstruct_path(parent, goal), explored

        if current_cost > cost.get(current, float('inf')):
            continue

        for neighbor in maze.get_connected_neighbors(*current):
            new_cost = current_cost + 1

            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(heap, (new_cost, neighbor))

    return None, explored


def a_star_search(maze, start, goal):
    g_score = {start: 0}
    f_score = manhattan_distance(start, goal)
    heap = [(f_score, 0, start)]
    parent = {start: None}
    explored = []

    while heap:
        _, current_g, current = heapq.heappop(heap)
        explored.append(current)

        if current == goal:
            return reconstruct_path(parent, goal), explored

        if current_g > g_score.get(current, float('inf')):
            continue

        for neighbor in maze.get_connected_neighbors(*current):
            tentative_g = current_g + 1

            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                parent[neighbor] = current
                f = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(heap, (f, tentative_g, neighbor))

    return None, explored
