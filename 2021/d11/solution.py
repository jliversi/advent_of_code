INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input_1.txt'
# INPUT_FILE = 'test_input_2.txt'

DIRS = (
    (-1,  0), # start at 12, go clockwise
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
    (-1, -1),
)

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return [[int(x) for x in row.strip()] for row in f.readlines()]

def display_grid(grid):
    print('------')
    print('')
    for row in grid:
        print(' '.join((str(x) for x in row)))
    print('')
    print('------')

def pt_in_grid(pt, grid):
    x,y = pt
    if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]):
        return True
    return False

def delta_pt(pt, dpt):
    return (pt[0] + dpt[0], pt[1] + dpt[1])

def neighbors(pt, grid):
    return [delta_pt(pt, dpt) for dpt in DIRS if pt_in_grid(delta_pt(pt, dpt), grid)]

def increment_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1

def find_first_flashers(grid):
    result = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] > 9: result.append((x,y))
    return result

def flash(flashers, flashed_this_turn, grid):
    next_flashers = []
    num_flashes = 0
    for f in flashers:
        flashed_this_turn.add(f)
    for f in flashers:
        ns = neighbors(f, grid)
        
        for neighbor in ns:
            grid[neighbor[0]][neighbor[1]] += 1
            if grid[neighbor[0]][neighbor[1]] > 9 and neighbor not in flashed_this_turn and neighbor not in next_flashers:
                next_flashers.append(neighbor)
        num_flashes += 1
    return (next_flashers, num_flashes)

def take_turn(grid):
    flash_count = 0
    flashed_this_turn = set()
    increment_grid(grid)
    next_flashers = find_first_flashers(grid)
    while next_flashers:
        next_flashers, num_flashes = flash(next_flashers, flashed_this_turn, grid)
        flash_count += num_flashes

    for flashed in flashed_this_turn:
        x,y = flashed
        grid[x][y] = 0
    return flash_count

def check_all_zeroes(grid):
    for row in grid:
        for x in row:
            if x != 0:
                return False
    return True

def part_one(grid):
    total_flash_count = 0
    for i in range(100):
        turn_flash_count = take_turn(grid)
        total_flash_count += turn_flash_count
    print(total_flash_count)
    
def part_two(grid):
    all_zeroes = False
    turn_count = 0
    while not all_zeroes:
        take_turn(grid)
        turn_count += 1
        all_zeroes = check_all_zeroes(grid)
    print(turn_count)

def main():
    grid = parse_input(INPUT_FILE)
    part_two(grid)

if __name__ == '__main__':
    main()