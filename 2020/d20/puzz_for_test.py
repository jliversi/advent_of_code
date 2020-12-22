from square import Square
import re
    
ALL = dict()
ALL_SIDE_NAMES = ('nT','nR','nB','nL','rT','rR','rB','rL')
SIDE_NAMES = ('T','R','B','L')

with open('test_input.txt') as f:
    for sqr_str in f.read().split('\n\n'):
        sqr = Square(sqr_str)
        ALL[sqr.sqr_id] = sqr


def all_poss_neighbors(subject_sqr_id):
    subject = ALL[subject_sqr_id]
    result = dict()
    for sqr_id in ALL:
        if sqr_id == subject_sqr_id:
            continue
        
        other_sqr = ALL[sqr_id]
        for variant, side_name in zip(other_sqr.all_poss_sides, ALL_SIDE_NAMES):
            for side, s_name in zip(subject.normal_sides, SIDE_NAMES):
                if side == variant:
                    result[sqr_id] = (s_name, side_name)
    
    subject.poss_neighbors = result
    return result

# Used in part 1 and in determining corners, sides, inners
def count_poss_neighbors(sqr_id):
    sqr = ALL[sqr_id]
    return len(sqr.poss_neighbors)


CORNERS = []
SIDES = []
INNERS = []

# Determine corners, sides and inners
for sqr_id in ALL:
    sqr = ALL[sqr_id]
    all_poss_neighbors(sqr_id)
    count_for_sqr = count_poss_neighbors(sqr_id)
    if count_for_sqr == 2:
        CORNERS.append(sqr)
    elif count_for_sqr == 3:
        SIDES.append(sqr)
    elif count_for_sqr == 4:
        INNERS.append(sqr)

FINAL_GRID = []
for i in range(3):
    row = [None] * 3
    FINAL_GRID.append(row)

def orient_sqr(sqr, rel_nbr):
    nbr_rule = rel_nbr.poss_neighbors[sqr.sqr_id]
    side_on_nbr, match_on_sqr = nbr_rule
    if side_on_nbr == 'R':
        rotation_list = ['L', 'B', 'R', 'T']
        to_match = rel_nbr.right
    else:
        rotation_list = ['T', 'L', 'B', 'R']
        to_match = rel_nbr.bottom

    for i in range(rotation_list.index(match_on_sqr[1])):
        sqr.rotate90()

        
    if side_on_nbr == 'R':
        if sqr.left != to_match:
            sqr.flip_y()
    else:
        if sqr.top != to_match:
            sqr.flip_x()
    

def increment_coords(coords):
    x, y = coords
    if y == 2:
        return (x + 1, 0)
    else:
        return (x, y + 1)

current_piece = CORNERS[0]
current_coords = (0,0)

# Start solving
while True:
    cur_x, cur_y = current_coords
    FINAL_GRID[cur_x][cur_y] = current_piece
    # finish after placing final piece
    if current_coords == (2,2):
        break

    # special logic for first piece (hardcoded orientation)
    if current_coords == (0,0):
        # hard codes, known orientation from input
        current_piece.flip_y()

    # redo neighbors to new known orientation
    all_poss_neighbors(current_piece.sqr_id)
    
    # determine where to look for next piece
    if cur_y == 2:
        rel_nbr = FINAL_GRID[cur_x][0]
        dir_to_find = 'B'
    else:
        rel_nbr = current_piece
        dir_to_find = 'R'

    new_poss_neighbors = rel_nbr.poss_neighbors


    # print(rel_nbr.sqr_id)
    # print(new_poss_neighbors)
    
    
    # find next piece 
    for k in new_poss_neighbors:
        if new_poss_neighbors[k][0] == dir_to_find:
            next_piece = ALL[k]
    

    # decide orientation of next piece
    # HARDEST PART TO PROGRAM! SO EASY AS A HUMAN! 
    orient_sqr(next_piece, rel_nbr)
    
    # prepare for next iteration
    current_piece = next_piece
    current_coords = increment_coords(current_coords)

# at this point, FINAL_GRID contains the completed 
ID_GRID = []
for row in FINAL_GRID:
    ids_row = []
    for el in row:
        ids_row.append(el.sqr_id)
    ID_GRID.append(ids_row)






# turn it into one big string
pre_final_string_grid = []
FINAL_STRING = ''
for row in FINAL_GRID:
    row_strs = [''] * 8
    for square in map(lambda x: x.trim_sides(), row):
        for i, minor_row in enumerate(square):
            row_strs[i] += ''.join(minor_row)
    
    FINAL_STRING += '\n'.join(row_strs)
    FINAL_STRING += '\n'

FINAL_STRING = FINAL_STRING[:-1]




# DRAGON_PATTERN = r'.{18}#..{5}#.{4}#{2}.{4}#{2}.{4}#{3}.{5}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}'

# def dragon_count(search_str):
#     found = re.findall(DRAGON_PATTERN, search_str, re.DOTALL)
#     total = 0
#     for el in found:
#         if el.count('\n') == 2:
#             total += 1
#     return total

# ALT DRAGON COUNT STRATEGY
# DRAGON_PATTERN_1 = r'#.{4}#{2}.{4}#{2}.{4}#{3}'
# DRAGON_PATTERN_2 = r'.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}'
# def dragon_count(search_str):
#     total = 0
#     line_length = len(search_str.split('\n')[0]) + 1
    
#     found = re.finditer(DRAGON_PATTERN_1, search_str, re.DOTALL)
#     for el in found:
#         start, end = el.span()
#         if start > 575:
#             continue
#         substring = search_str[start:end]
#         if '\n' in substring:
#             continue
#         if search_str[end - line_length - 2] != '#':
#             continue
#         next_line = search_str[start + line_length:end + line_length]
#         next_line_found = re.search(DRAGON_PATTERN_2, next_line, re.DOTALL)
#         if next_line_found:
#             total += 1
#     return total

IDXS_TO_CHECK = [0, 7, 5, 1, 5, 1, 5, 1, 1, 7, 3, 3, 3, 3, 3]
TOTAL_RANGE = sum(IDXS_TO_CHECK)
def check_char(idx, search_str):
    for di in IDXS_TO_CHECK:
        if search_str[idx + di] != '#':
            return False
    return search_str[idx:idx+TOTAL_RANGE].count('\n') == 2

def dragon_count(search_str):
    total = 0
    for i in range(len(search_str) - TOTAL_RANGE):
        if check_char(i, search_str):
            total += 1
    return total



def flip_str_y():
    new_str = ''
    for l in reversed(FINAL_STRING.split('\n')):
        new_str += l
        new_str += '\n'
    return new_str[:-1]


def rotate_str_90():
    new_str = ''
    split_str = FINAL_STRING.split('\n')
    for i in range(len(split_str)):
        new_row = ''.join(reversed([list(x)[i] for x in split_str]))
        new_str += new_row
        new_str += '\n'
    return new_str[:-1]


possible_orientations = []
# normal orientations
for i in range(4):
    possible_orientations.append(FINAL_STRING)
    FINAL_STRING = rotate_str_90()

# flipped orientations
FINAL_STRING = flip_str_y()
for i in range(4):
    possible_orientations.append(FINAL_STRING)
    FINAL_STRING = rotate_str_90()


for el in possible_orientations:
    count = dragon_count(el)
    print(count)
    if count > 0:
        TRUE_FINAL_STRING = el
        TRUE_DRAGON_COUNT = count

hash_count = 0
for char in TRUE_FINAL_STRING:
    if char == '#':
        hash_count += 1


print(hash_count - (TRUE_DRAGON_COUNT * 15))


