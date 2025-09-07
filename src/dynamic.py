import os
from datetime import datetime
from .algorithms import hill_climbing, simulated_annealing, a_star

LOG_FILE = os.path.join("results", "logs", "run_log.txt")


class DynamicAgent:
    def __init__(self, grid, start, goal, strategy="hill_climbing"):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.strategy = strategy
        self.path = self.plan_path(start)

        # Ensure logs directory exists
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(
                f"\n--- New Run [{datetime.now()}] | Strategy: {self.strategy} ---\n"
            )

    def plan_path(self, start):
        if self.strategy == "a_star":
            path, _ = a_star(self.grid, start, self.goal)
        elif self.strategy == "hill_climbing":
            path = hill_climbing(self.grid, start, self.goal)
        elif self.strategy == "simulated_annealing":
            path = simulated_annealing(self.grid, start, self.goal)
        else:
            raise ValueError("Unknown strategy")
        return path

    def move(self):
        while self.path:
            current = self.path.pop(0)
            if not self.grid.is_valid(*current):
                msg = f"Obstacle detected at {current}. Replanning path..."
                print(msg)
                with open(LOG_FILE, "a") as f:
                    f.write(msg + "\n")

                self.path = self.plan_path(current)
                if not self.path:
                    msg = "No path found. Delivery failed!"
                    print(msg)
                    with open(LOG_FILE, "a") as f:
                        f.write(msg + "\n")
                    return False
            else:
                msg = f"Moving to {current}"
                print(msg)
                with open(LOG_FILE, "a") as f:
                    f.write(msg + "\n")

        msg = "Package delivered successfully!"
        print(msg)
        with open(LOG_FILE, "a") as f:
            f.write(msg + "\n")
        return True
