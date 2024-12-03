# INPUT_FILE = 'input.txt'
INPUT_FILE = 'test_input.txt'

def parse_input(file_name):
    with open(file_name, 'r') as f:
        start, rules = f.read().split('\n\n')
        rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1].strip() for rule in rules.split('\n')}
        return start.strip(), rules

def part_one_step(string, rules):
    insertions = dict()
    # build insertions
    for i in range(len(string) - 1):
        substr = string[i:i+2]
        if substr in rules:
            insertions[i] = rules[substr]
    new_str = []
    for i in range(len(string)):
        new_str.append(string[i])
        if i in insertions: new_str.append(insertions[i])
    return ''.join(new_str)

def string_to_char_pairs(string):
    result = dict()
    for i in range(len(string) - 1):
        char_pair = string[i:i+2]
        result[char_pair] = result.get(char_pair, 0) + 1
    return result

def char_pairs_to_count_dict(char_pairs, first_char, last_char):
    count = dict()
    for char_pair, amt in char_pairs.items():
        for char in char_pair:
            count[char] = count.get(char,0) + (amt / 2)
    count[first_char] += 1
    count[last_char] += 1
    return count

def step(char_pairs, rules):
    result = dict()
    for pair in char_pairs:
        if pair in rules:
            amt = char_pairs[pair]
            x = pair[0] + rules[pair]
            y = rules[pair] + pair[1]
            result[x] = result.get(x, 0) + amt
            result[y] = result.get(y, 0) + amt
        else:
            result[pair] = char_pairs[pair]
    return result

def part_one(start, rules):
    polymer_string = start
    for i in range(10):
        polymer_string = part_one_step(polymer_string, rules)
    char_count = {}
    for char in polymer_string:
        char_count[char] = char_count.get(char, 0) + 1
    answer = max(char_count.values()) - min(char_count.values())
    print(answer)

def part_two(start, rules):
    first_char, last_char = start[0], start[-1]
    char_pairs = string_to_char_pairs(start)
    for i in range(40):
        print('Working on step ', i+1, '...')
        char_pairs = step(char_pairs, rules)
    # print(char_pairs)
    char_count = char_pairs_to_count_dict(char_pairs, first_char, last_char)
    # print(char_count)
    answer = max(char_count.values()) - min(char_count.values())
    print(answer)

def main():
    start, rules = parse_input(INPUT_FILE)
    # part_one(start, rules)
    part_two(start, rules)

if __name__ == '__main__':
    main()