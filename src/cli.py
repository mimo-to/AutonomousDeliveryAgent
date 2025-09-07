import argparse
from grid import Grid
from algorithms import bfs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", type=str, required=True)
    parser.add_argument("--algorithm", type=str, choices=["bfs"], required=True)
    args = parser.parse_args()

    grid = Grid(args.map)
    start = goal = None

    for i in range(grid.rows):
        for j in range(grid.cols):
            if grid.grid[i][j] == "S":
                start = (i, j)
            if grid.grid[i][j] == "G":
                goal = (i, j)

    print("Start:", start)
    print("Goal:", goal)

    if args.algorithm == "bfs":
        path = bfs(grid, start, goal)
        if path:
            print("Path found:", path)
        else:
            print("No path found")


if __name__ == "__main__":
    main()
