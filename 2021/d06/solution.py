INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

# def part_1_parse_input(file_name):
#     with open(file_name, 'r') as f:
#         return [int(x) for x in f.read().split(',')]

# def part_1_turn(fish_arr):
#     result_arr = fish_arr.copy()
#     for i, fish in enumerate(fish_arr):
#         next_num = fish - 1
#         if next_num < 0:
#             next_num = 6
#             result_arr.append(8)
#         result_arr[i] = next_num
#     return result_arr

# def part_1():
#     fish_arr = part_1_parse_input(INPUT_FILE)
#     for i in range(10):
#         fish_arr = part_1_turn(fish_arr)
#     print(len(fish_arr))

def parse_input(file_name):
    result = dict()
    with open(file_name, 'r') as f:
        for x in f.read().split(','):
            num = int(x)
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
    return result

def take_turn(fish_dict):
    result = {}
    for i in reversed(range(9)):
        if i > 0:
            if i in fish_dict:
                result[i - 1] = fish_dict[i]
        else:
            if 0 in fish_dict:
                result[8] = fish_dict[0]
                if 6 in result:
                    result[6] += fish_dict[0]
                else:
                    result[6] = fish_dict[0]
    return result

def main():
    fish_dict = parse_input(INPUT_FILE)
    for i in range(256):
        # print(fish_dict)
        fish_dict = take_turn(fish_dict)
    # print(fish_dict)
    print(sum(fish_dict.values()))


# for part 2, refactor to just keep a count of current num fish at any given number

if __name__ == '__main__':
    main()