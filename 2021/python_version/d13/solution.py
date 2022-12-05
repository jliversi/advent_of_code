INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

def parse_input(file_name):
    with open(file_name, 'r') as f:
        pts, folds = f.read().split('\n\n')
        pts = [tuple([int(x.strip()) for x in pt.split(',')]) for pt in pts.split('\n')]
        folds = [fold_line.split(' ')[2].split('=') for fold_line in folds.split('\n')]
        for f in folds: f[1] = int(f[1])
    return pts, folds

def print_page(pts):
    max_x = max(pt[0] for pt in pts) + 1
    max_y = max(pt[1] for pt in pts) + 1
    line_list = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for pt in pts:
        x,y = pt
        line_list[y][x] = '#'
    for line in line_list:
        print(''.join(line))

def fold_over_hor(pt, line_num):
    x,y = pt
    if y <= line_num:
        return pt
    new_y = line_num - (y - line_num)
    return (x,new_y)

def fold_over_ver(pt, line_num):
    x,y = pt
    if x <= line_num:
        return pt
    new_x = line_num - (x - line_num)
    return (new_x,y)

def fold_pt(pt, fold):
    if fold[0] == 'y':
        return fold_over_hor(pt, fold[1])
    elif fold[0] == 'x':
        return fold_over_ver(pt, fold[1])

def fold_page(pts, fold):
    folded_pts = set()
    for pt in pts:
        folded_pts.add(fold_pt(pt, fold))
    return folded_pts

def part_one(pts, first_fold):
    folded_pts = fold_page(pts, first_fold)
    print(len(folded_pts))

def part_two(pts, folds):
    for fold in folds:
        pts = fold_page(pts, fold)
    print_page(pts)

def main():
    pts, folds = parse_input(INPUT_FILE)
    part_two(pts, folds)

if __name__ == '__main__':
    main()