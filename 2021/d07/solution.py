
INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

def parse_input(file_name):
    with open(file_name, 'r') as f:
        return [int(x) for x in f.read().split(',')]

def calc_cost_pt_1(nums, align_pos):
    total = 0
    for num in nums:
        total += abs(num - align_pos)
    return total

def calc_one_cost(num, align_pos):
    dist = abs(num - align_pos)
    if dist % 2 == 0:
        return (dist // 2) * (dist + 1)
    else:
         return ((dist - 1) // 2) * ((dist - 1) + 1) + dist


def calc_total_cost(nums, align_pos):
    total = 0
    for num in nums:
        total += calc_one_cost(num, align_pos)
    return total

def main():
    nums = parse_input(INPUT_FILE)
    minimum = min(nums)
    maximum = max(nums)
    costs = []
    for i in range(minimum, maximum):
        costs.append(calc_total_cost(nums,i))
    print(min(costs))

if __name__ == '__main__':
    main()