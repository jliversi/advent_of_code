from functools import cache

INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return [[int(x) for x in row.strip()] for row in f.readlines()]

def find_low_points(grid):
    low_points = []
    for x, row in enumerate(grid):
        for y, num in enumerate(row):
            ns = neighbor_nums(x,y,grid)
            if num < min(ns): low_points.append((x,y))
    return low_points


def neighbor_nums(x,y,grid):
    h, w = len(grid) - 1, len(grid[0]) - 1
    result = []
    if x > 0: result.append(grid[x-1][y])
    if y > 0: result.append(grid[x][y-1])
    if x < h: result.append(grid[x+1][y])
    if y < w: result.append(grid[x][y+1])
    return result

def neighbor_pts(x,y,grid):
    h, w = len(grid) - 1, len(grid[0]) - 1
    result = []
    if x > 0: result.append((x-1,y))
    if y > 0: result.append((x,y-1))
    if x < h: result.append((x+1,y))
    if y < w: result.append((x,y+1))
    return result

def smallest_neighbor_pt(pt, grid):
    x,y = pt
    ns = neighbor_pts(x,y,grid)
    min = grid[x][y]
    min_pt = pt
    for x2,y2 in ns:
        if grid[x2][y2] < min:
            min = grid[x2][y2]
            min_pt = (x2,y2)
    return min_pt


def find_basin_bottom(pt,low_points,grid):
    if pt in low_points: return pt
    
    x,y = pt 
    if grid[x][y] == 9: return None
    next_pt = smallest_neighbor_pt(pt,grid)
    return find_basin_bottom(next_pt,low_points,grid)

def part_one():
    low_pt_vals = [grid[x][y] for x,y in low_points]
    total = sum(low_pt_vals) + len(low_pt_vals)
    print(total)

def part_two(basin_dict):
    basin_dict[None] = 0
    big_3 = sorted(list(basin_dict.values()))[-3:]
    print(big_3[0] * big_3[1] * big_3[2])

def main():
    grid = parse_input(INPUT_FILE)
    low_points = find_low_points(grid)
    basin_dict = {None: 0}
    for pt in low_points:
        basin_dict[pt] = 0
    for x, row in enumerate(grid):
        for y, num in enumerate(row):
            basin = find_basin_bottom((x,y),low_points,grid)
            basin_dict[basin] += 1
    part_two(basin_dict)

if __name__ == '__main__':
    main()