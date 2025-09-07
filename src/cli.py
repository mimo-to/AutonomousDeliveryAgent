import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.grid import Grid
from src.algorithms import bfs, ucs, a_star
from src.dynamic import DynamicAgent


def main():
    parser = argparse.ArgumentParser(
        description="Run pathfinding algorithms on a grid."
    )
    parser.add_argument("--map", type=str, required=True, help="Path to map file")
    parser.add_argument(
        "--algorithm",
        type=str,
        choices=["bfs", "ucs", "a_star", "hill_climbing", "simulated_annealing"],
        required=True,
        help="Algorithm to use",
    )
    args = parser.parse_args()

    grid = Grid(args.map)
    start = (grid.start_x, grid.start_y)
    goal = (grid.goal_x, grid.goal_y)

    print("Start:", start)
    print("Goal:", goal)

    if args.algorithm == "bfs":
        path = bfs(grid, start, goal)
        print("Path found:", path if path else "No path found")
    elif args.algorithm == "ucs":
        path, cost = ucs(grid, start, goal)
        if path:
            print("Path found:", path)
            print("Total cost:", cost)
        else:
            print("No path found")
    elif args.algorithm == "a_star":
        path, cost = a_star(grid, start, goal)
        if path:
            print("Path found:", path)
            print("Total cost:", cost)
        else:
            print("No path found")
    else:
        agent = DynamicAgent(grid, start, goal, strategy=args.algorithm)
        agent.move()


if __name__ == "__main__":
    main()
