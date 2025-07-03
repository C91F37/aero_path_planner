import heapq

# ========================
# A* Pathfinding Skeleton
# ========================

# Task 0: Define data structure to represent nodes (start, goal, and grid map)

# Task 1: Heuristic function
# Input: current node, goal node
# Output: estimated cost (float)


def heuristic(node, goal):
    """
    Calculate heuristic cost between current node and goal.
    Common: Manhattan, Euclidean, Diagonal
    I am assuming Manhattan and not Chebyshev or Minkowski, given is a 2d env
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Task 2: Get neighbour nodes (up, down, left, right, or 8 directions)
# Input: current node, map/grid
# Output: list of neighbour nodes that are not obstacles


def get_neighbours(node, grid):
    """
    Return valid neighbours of a given node (not blocked by obstacles).
    """
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = node[0] + dx, node[1] + dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            if grid[nx, ny] == 0:
                neighbours.append((nx, ny))
    return neighbours

# Task 3: Reconstruct path from came_from dict
# Input: came_from (dict of node: parent), current node
# Output: list of path nodes from start to goal


def reconstruct_path(came_from, current):
    """
    Reconstruct path from goal to start using parent mapping.
    """
    if current not in came_from:
        return [current]
    return reconstruct_path(came_from, came_from[current]) + [current]


# Task 4: Main A* function
# Input: grid map, start node, goal node
# Output: path (list of nodes), or None if not found


def astar(grid, start, goal):
    """
    Core A* algorithm loop:
    - Initialize open list (priority queue)
    - Initialize g_costs (actual cost to reach node)
    - Initialize came_from mapping (for path reconstruction)
    - Loop:
        - Pop node with lowest f(ull) = g(actual distance from start to current) + h(euristic)
        - If goal, reconstruct path
        - Else, explore neighbours and update costs
    """

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), start))
    came_from = {}
    g = {start: 0}

    while open_set:
        current_f, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbour in get_neighbours(current, grid):
            tentative_g = g[current] + 1
            if neighbour not in g or tentative_g < g[neighbour]:
                came_from[neighbour] = current
                g[neighbour] = tentative_g
                f = tentative_g + heuristic(neighbour, goal)
                heapq.heappush(open_set, (f, neighbour))

    return None
