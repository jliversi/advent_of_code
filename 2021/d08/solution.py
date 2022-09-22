
# INPUT_FILE = 'test_input_1.txt'
# INPUT_FILE = 'test_input_2.txt'
INPUT_FILE = 'input.txt'

def parse_input(file_name):
    with open(file_name, 'r') as f:
        lines = [x.split('|') for x in f.readlines()]
    return [[a.strip().split(' '), b.strip().split(' ')] for a, b in lines]

def part_1():
    input = parse_input(INPUT_FILE)
    total = 0
    for x in input:
        for y in x[1]:
            if len(y) in [2,3,4,7]:
                total += 1
    print(total)

#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg

# letter finders
def find_a(one, seven):
    for char in 'abcdefg':
        if char in seven and char not in one:
            return char

def find_b(three, four, eight):
    for char in 'abcdefg':
        if char not in three and char in eight and char in four:
            return char

def find_c(two, five, e):
    # print(two, five, e)
    for char in two:
        # print(char)
        # print(char not in five)
        if char not in five and char != e:
            # print(char)
            return char

def find_d(one, four, seven, eight):
    for char in 'abcdefg':
        pass

def find_e(three, four, eight):
    for char in 'abcdefg':
        if char not in three and char in eight and char not in four:
            return char

def find_f(one, c):
    for char in one:
        if char != c:
            return char
        
# num finders
def find_three(nums, one):
    x, y = one
    for num in nums:
        if len(num) == 5 and x in num and y in num:
            return num

def find_two(nums, three, e):
    for num in nums:
        if len(num) == 5 and num != three and e in num:
            return num

def find_five(nums, two, three):
    for num in nums:
        if len(num) == 5 and num != two and num != three:
            return num

def find_six(nums, c):
    for num in nums:
        if len(num) == 6 and c not in num:
            return num

def find_nine(nums, e):
    for num in nums:
        if len(num) == 6 and e not in num:
            return num

def find_zero(nums, six, nine):
    for num in nums:
        if len(num) == 6 and num != six and num != nine:
            return num

def solve_nums(nums):
    sides = {}
    nums_solved = [None] * 10
    nums_solved[1] = [x for x in nums if len(x) == 2][0]
    nums_solved[4] = [x for x in nums if len(x) == 4][0]
    nums_solved[7] = [x for x in nums if len(x) == 3][0]
    nums_solved[8] = [x for x in nums if len(x) == 7][0]
    nums_solved[3] = find_three(nums, nums_solved[1])
    nums_solved[3] = find_three(nums, nums_solved[1])

    sides['a'] = find_a(nums_solved[1], nums_solved[7])
    sides['b'] = find_b(nums_solved[3], nums_solved[4], nums_solved[8])

    sides['e'] = find_e(nums_solved[3], nums_solved[4], nums_solved[8])
    nums_solved[2] = find_two(nums, nums_solved[3], sides['e'])
    nums_solved[5] = find_five(nums, nums_solved[2], nums_solved[3])

    sides['c'] = find_c(nums_solved[2], nums_solved[5], sides['e'])
    sides['f'] = find_f(nums_solved[1], sides['c'])

    nums_solved[6] = find_six(nums, sides['c'])
    nums_solved[9] = find_nine(nums, sides['e'])
    nums_solved[0] = find_zero(nums, nums_solved[6],  nums_solved[9])

    return list(map(lambda x: sorted(x), nums_solved))


def decode_line(line):
    # nums
    # ['dg', 'debg', 'edgfc', 'afbgcd', 'efdbgc', 'gdc', 'bfdceag', 'bfdec', 'febcad', 'gfaec']
    # code
    # ['dcg', 'bdaegfc', 'egbd', 'dcgfe']
    nums, code = line
    nums_solved = solve_nums(nums)
    digits = [str(nums_solved.index(sorted(dig))) for dig in code]
    return int(''.join(digits))




def main():
    lines = parse_input(INPUT_FILE)
    print(sum([decode_line(l) for l in lines]))



if __name__ == '__main__':
    main()