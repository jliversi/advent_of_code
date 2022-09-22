INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

def process_row(row, coord_dict):
    x1, y1 = row[0]
    x2, y2 = row[1]
    next_x = x1
    next_y = y1
    while next_x != x2 or next_y != y2:
        coord = (next_x, next_y)
        if coord in coord_dict:
            coord_dict[coord] += 1
        else:
            coord_dict[coord] = 1
        if next_x < x2:
            next_x += 1
        elif next_x > x2:
            next_x -= 1
        if next_y < y2:
            next_y += 1
        elif next_y > y2:
            next_y -= 1
    coord = (next_x, next_y)
    if coord in coord_dict:
        coord_dict[coord] += 1
    else:
        coord_dict[coord] = 1

def parse_input(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            a,b = line.split(' -> ')
            result.append(([int(x) for x in a.split(',')], [int(x) for x in b.split(',')]))
    return result

def main():
    rows = parse_input(INPUT_FILE)
    coord_dict = {}
    for row in rows:
        process_row(row, coord_dict)
    print(len([True for k in coord_dict if coord_dict[k] > 1]))


if __name__ == '__main__':
    main()