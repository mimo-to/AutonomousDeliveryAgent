class Grid:
    def __init__(self, filename):
        self.grid = self.load_grid(filename)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        print("Loaded Grid:")
        for row in self.grid:
            print("".join(row))

    def load_grid(self, filename):
        grid = []
        with open(filename, "r") as f:
            for line in f:
                grid.append(list(line.strip()))
        return grid

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != "#"

    def print_grid(self):
        for row in self.grid:
            print("".join(row))
