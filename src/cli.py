import argparse
from grid import Grid
from algorithms import bfs, ucs, a_star


def main():
    parser = argparse.ArgumentParser(
        description="Run pathfinding algorithms on a grid."
    )
    parser.add_argument("--map", type=str, required=True, help="Path to map file")
    parser.add_argument(
        "--algorithm",
        type=str,
        choices=["bfs", "ucs", "a_star"],
        required=True,
        help="Algorithm to use",
    )
    args = parser.parse_args()

    try:
        grid = Grid(args.map)
        start = (grid.start_x, grid.start_y)
        goal = (grid.goal_x, grid.goal_y)

        print("Start:", start)
        print("Goal:", goal)
        # BFS
        if args.algorithm == "bfs":
            path = bfs(grid, start, goal)
            if path:
                print("Path found:", path)
            else:
                print("No path found")
        # UCS
        elif args.algorithm == "ucs":
            path, cost = ucs(grid, start, goal)
            if path:
                print("Path found:", path)
                print("Total cost:", cost)
            else:
                print("No path found")
        # A*
        elif args.algorithm == "a_star":
            path, cost = a_star(grid, start, goal)
            if path:
                print("Path found:", path)
                print("Total cost:", cost)
            else:
                print("No path found")
    except FileNotFoundError:
        print("Map file not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
