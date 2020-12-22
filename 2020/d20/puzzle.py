from square import Square
import re
    
ALL = dict()
ALL_SIDE_NAMES = ('nT','nR','nB','nL','rT','rR','rB','rL')
SIDE_NAMES = ('T','R','B','L')

with open('input.txt') as f:
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
for i in range(12):
    row = [None] * 12
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
    if y == 11:
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
    if current_coords == (11,11):
        break

    # special logic for first piece (hardcoded orientation)
    if current_coords == (0,0):
        # hard codes, known orientation from input
        current_piece.rotate90()

    # redo neighbors to new known orientation
    all_poss_neighbors(current_piece.sqr_id)
    
    # determine where to look for next piece
    if cur_y == 11:
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


# FOR TESTING, CREATE FULL GRID WITH DIVIDERS, MAKE SURE YOU PUT TOGETHER CORRECTLY
# GRID_STRING = ''
# for row in FINAL_GRID:
#     for i in range(10):
#         for el in row:
#             GRID_STRING += ''.join(el.grid[i])
#             GRID_STRING += '|'
#         GRID_STRING += '\n'
#     GRID_STRING += ('-' * 129) 
#     GRID_STRING += '\n'

# print(GRID_STRING)


# turn it into one big string
FINAL_STRING = ''
for row in FINAL_GRID:
    row_strs = [''] * 8
    for square in map(lambda x: x.trim_sides(), row):
        for i, minor_row in enumerate(square):
            row_strs[i] += ''.join(minor_row)
    
    FINAL_STRING += '\n'.join(row_strs)
    FINAL_STRING += '\n'

FINAL_STRING = FINAL_STRING[:-1]


# DRAGON_PATTERN = r'[#.]{18}#[#.][.#\n]{77}#[#.]{4}#{2}[#.]{4}#{2}[#.]{4}#{3}[.#\n]{77}[#.]#[#.]{2}#[#.]{2}#[#.]{2}#[#.]{2}#[#.]{2}#[#.]{3}'

# def dragon_count(search_str):
#     return len(re.findall(DRAGON_PATTERN, search_str))

#     found = re.findall(DRAGON_PATTERN, search_str)
#     total = 0
#     for el in found:
#         if el.count('\n') == 2:
#             total += 1
#     return total

# ALT DRAGON COUNT STRATEGY
DRAGON_PATTERN_1 = r'..................#.'
DRAGON_PATTERN_2 = r'#....##....##....###'
DRAGON_PATTERN_3 = r'.#..#..#..#..#..#...'
def dragon_count(search_str):
    total = 0
    search_arr = search_str.split('\n')
    for i in range(len(search_arr) - 2):
        line1 = search_arr[i]
        line2 = search_arr[i + 1]
        line3 = search_arr[i + 2]
        for j in range(len(line1) - 20 + 1):
            substr1 = line1[j:j+21]
            if re.match(DRAGON_PATTERN_1, substr1):
                substr2 = line2[j:j+21]
                if re.match(DRAGON_PATTERN_2, substr2):
                    substr3 = line3[j:j+21]
                    if re.match(DRAGON_PATTERN_3, substr3):
                        total += 1

    return total

# THIRD, Kinda silly, dragon count strategy
# IDXS_TO_CHECK = [0, 79, 5, 1, 5, 1, 5, 1, 1, 79, 3, 3, 3, 3, 3]
# TOTAL_RANGE = sum(IDXS_TO_CHECK)
# def check_char(idx, search_str):
#     for di in IDXS_TO_CHECK:
#         if search_str[idx + di] != '#':
#             return False
#     return search_str[idx:idx+TOTAL_RANGE].count('\n') == 2

# def dragon_count(search_str):
#     total = 0
#     for i in range(len(search_str) - TOTAL_RANGE):
#         if check_char(i, search_str):
#             total += 1
#     return total


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
    if count > 0:
        TRUE_FINAL_STRING = el
        TRUE_DRAGON_COUNT = count



hash_count = TRUE_FINAL_STRING.count('#')
num_hash_in_dragons = 15 * TRUE_DRAGON_COUNT
print(hash_count)
print(TRUE_DRAGON_COUNT)
print(num_hash_in_dragons)
print(hash_count - num_hash_in_dragons)



# matches = re.finditer(DRAGON_PATTERN, TRUE_FINAL_STRING, re.DOTALL)
# for el in matches:
#     print(el.span())





# def flip_str_x():
#     new_str = ''
#     for l in FINAL_STRING.split('\n'):
#         new_str += ''.join(reversed(l))
#         new_str += '\n'
#     return new_str[:-1]


# print(len(possible_orientations))
# uniqs = set()
# for el in possible_orientations:
#     if el not in uniqs:
#         uniqs.add(el)

# print(len(uniqs))

# a = possible_orientations[5]
# b = possible_orientations[15]

# print(a)
# print('-')
# print(b)
# print(a == b)

# for i, el1 in enumerate(possible_orientations):
#     for j, el2 in enumerate(possible_orientations):
#         if i != j:
#             if el1 == el2:
#                 print('found dup!')

# for el in possible_orientations:
#     print('-------')
#     print('-------')
#     print(el)






# PART 1 ANSWR
# final_result = 1
# for sqr_id in ALL:
#     sqr = ALL[sqr_id]
#     all_poss_neighbors(sqr_id)
#     count_for_sqr = count_poss_neighbors(sqr_id)
#     if count_for_sqr == 2:
#         final_result *= sqr_id

# print(final_result)

