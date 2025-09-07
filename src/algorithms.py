from collections import deque
import heapq


# BFS
def bfs(grid, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return reconstruct_path(parent, goal)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if grid.is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))
    return None


# UCS
def ucs(grid, start, goal):
    pq = [(0, start)]
    visited = set()
    parent = {start: None}
    cost_so_far = {start: 0}

    while pq:
        cost, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            return reconstruct_path(parent, goal), cost

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if grid.is_valid(nx, ny):
                new_cost = cost_so_far[(x, y)] + grid.get_cost(nx, ny)
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_cost, (nx, ny)))

    return None, float("inf")


# A* with Manhattan heuristic
def a_star(grid, start, goal):
    pq = [(0, start)]
    cost_so_far = {start: 0}
    parent = {start: None}
    visited = set()

    while pq:
        f_score, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            return reconstruct_path(parent, goal), cost_so_far[(x, y)]

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if grid.is_valid(nx, ny):
                new_cost = cost_so_far[(x, y)] + grid.get_cost(nx, ny)
                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    parent[(nx, ny)] = (x, y)
                    h = abs(goal[0] - nx) + abs(goal[1] - ny)
                    f_score = new_cost + h
                    heapq.heappush(pq, (f_score, (nx, ny)))

    return None, float("inf")


def reconstruct_path(parent, goal):
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path
