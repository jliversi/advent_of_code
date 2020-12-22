class Square:
    def __init__(self, input):
        self.input = input
        self.setup_id()
        self.setup_grid()
        self.setup_sides()
        self.setup_side_variants()
        self.poss_neighbors = None
        self.true_dir = None
    
    def setup_id(self):
        self.sqr_id = int(self.input[5:9])

    def setup_grid(self):
        self.grid = []
        for el in self.input.split('\n')[1:]:
            self.grid.append(list(el))

    def setup_sides_partial(self):
        self.top = self.grid[0][:]
        self.right = [x[9] for x in self.grid]
        self.bottom = self.grid[9][:]
        self.left = [x[0] for x in self.grid]
    
    def setup_sides(self):
        self.top = self.grid[0][:]
        self.right = [x[9] for x in self.grid]
        self.bottom = self.grid[9][:]
        self.left = [x[0] for x in self.grid]

        self.r_top = list(reversed(self.top))
        self.r_right = list(reversed(self.right))
        self.r_bottom = list(reversed(self.bottom))
        self.r_left = list(reversed(self.left))

        self.normal_sides = [
            self.top,
            self.right,
            self.bottom,
            self.left
        ]
        self.all_poss_sides = [
            self.top,
            self.right,
            self.bottom,
            self.left,
            self.r_top,
            self.r_right,
            self.r_bottom,
            self.r_left
        ]
    
    def setup_side_variants(self):
        self.side_variants = [
            # normal
            [self.top, self.right, self.bottom, self.left],
            # vertical flip
            [self.bottom, self.r_right, self.top, self.r_left],
            # horizontal flip
            [self.r_top, self.left, self.r_bottom, self.right]
        ]
    
    def flip_y(self):
        new_grid = []
        for row in reversed(self.grid):
            new_grid.append(row)
        self.grid = new_grid
        self.setup_sides()
        self.setup_side_variants()

    def flip_x(self):
        new_grid = []
        for row in self.grid:
            new_grid.append(list(reversed(row)))
        self.grid = new_grid
        self.setup_sides()
        self.setup_side_variants()

    def rotate90(self):
        new_grid = []
        for i in range(len(self.grid)):
            new_row = list(reversed([x[i] for x in self.grid]))
            new_grid.append(new_row)
        self.grid = new_grid
        self.setup_sides()
        self.setup_side_variants()
        
    def trim_sides(self):
        return [x[1:9] for x in self.grid[1:9]]