import argparse
import os
import time
from datetime import datetime
from src.grid import Grid
from src.algorithms import bfs, ucs, a_star
from src.dynamic import DynamicAgent

LOG_FILE = os.path.join("results", "logs", "run_log.txt")


def ensure_log_dir():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


def log_run(algorithm, mapfile, path=None, cost=None, runtime=None, dynamic=False):
    """Append results to run_log.txt"""
    ensure_log_dir()
    with open(LOG_FILE, "a") as f:
        f.write(
            f"\n--- Run [{datetime.now()}] | Algo: {algorithm} | Map: {mapfile} ---\n"
        )
        if path:
            f.write(f"Path length: {len(path)}\n")
            f.write(f"Path: {path}\n")
        else:
            f.write("No path found\n")
        if cost is not None:
            f.write(f"Total cost: {cost}\n")
        if runtime is not None:
            f.write(f"Runtime: {runtime:.6f} seconds\n")
        if dynamic:
            f.write("Dynamic replanning was enabled.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Autonomous Delivery Agent: Run pathfinding algorithms on a grid."
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

    # --- Static algorithms ---
    if args.algorithm == "bfs":
        t0 = time.perf_counter()
        path = bfs(grid, start, goal)
        runtime = time.perf_counter() - t0
        if path:
            print("Path found:", path)
        else:
            print("No path found")
        log_run("bfs", args.map, path, runtime=runtime)

    elif args.algorithm == "ucs":
        t0 = time.perf_counter()
        path, cost = ucs(grid, start, goal)
        runtime = time.perf_counter() - t0
        if path:
            print("Path found:", path)
            print("Total cost:", cost)
        else:
            print("No path found")
        log_run("ucs", args.map, path, cost, runtime)

    elif args.algorithm == "a_star":
        t0 = time.perf_counter()
        path, cost = a_star(grid, start, goal)
        runtime = time.perf_counter() - t0
        if path:
            print("Path found:", path)
            print("Total cost:", cost)
        else:
            print("No path found")
        log_run("a_star", args.map, path, cost, runtime)

    # --- Dynamic algorithms ---
    else:
        agent = DynamicAgent(grid, start, goal, strategy=args.algorithm)
        success = agent.move()
        log_run(args.algorithm, args.map, path=agent.path, dynamic=True)


if __name__ == "__main__":
    main()
