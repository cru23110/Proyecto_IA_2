def reconstruct_path(parent_map, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent_map[current]
    path.reverse()
    return path


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
