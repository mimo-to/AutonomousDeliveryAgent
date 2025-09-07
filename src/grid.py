class Grid:
    def __init__(self, filename):
        self.dynamic_obstacles = {}
        self.grid = self.load_grid(filename)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.start_x, self.start_y, self.goal_x, self.goal_y = self.find_start_goal()
        print("Loaded Grid:")
        for row in self.grid:
            print(" ".join(map(str, row)))

    def load_grid(self, filename):
        grid = []
        with open(filename, "r") as f:
            dims = list(map(int, f.readline().strip().split()))
            (
                self.rows,
                self.cols,
                self.start_x,
                self.start_y,
                self.goal_x,
                self.goal_y,
            ) = dims[:6]
            for line in f:
                if line.strip():
                    row = []
                    for char in line.strip():
                        if char == "S":
                            row.append(1)  # Start as traversable
                        elif char == "G":
                            row.append(1)  # Goal as traversable
                        elif char == "#":
                            row.append(float("inf"))  # Obstacle
                        elif char.isdigit():
                            row.append(int(char))  # Numeric cost
                        else:
                            row.append(1)  # Default traversable
                    grid.append(row)
        return grid

    def find_start_goal(self):
        # Use header values for now, could scan grid if needed
        return self.start_x, self.start_y, self.goal_x, self.goal_y

    def is_valid(self, x, y, time=0):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            return False
        if self.grid[x][y] == float("inf") or (x, y) in self.dynamic_obstacles.get(
            time, set()
        ):
            return False
        return True

    def get_cost(self, x, y):
        return (
            self.grid[x][y]
            if 0 <= x < self.rows and 0 <= y < self.cols
            else float("inf")
        )

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
