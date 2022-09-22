INPUT_FILE = 'input.txt'
# INPUT_FILE = 'test_input.txt'

OPENS = ('(','[','{','<')
CLOSES = (')',']','}','>')
SYM_MAP = {}
for i in range(4):
    SYM_MAP[OPENS[i]] = CLOSES[i]
    SYM_MAP[CLOSES[i]] = OPENS[i]


def parse_input(file_name):
    with open(file_name, 'r') as f:
        return [x.strip() for x in f.readlines()]

def first_failing_char(line):
    recent_opens = []
    for char in line:
        if char in OPENS:
            recent_opens.append(char)
        elif char in CLOSES:
            if recent_opens:
                last_open = recent_opens.pop()
                if char != SYM_MAP[last_open]:
                    return char
            else:
                return char

def incomplete_opens(line):
    recent_opens = []
    for char in line:
        if char in OPENS:
            recent_opens.append(char)
        elif char in CLOSES:
            if recent_opens:
                last_open = recent_opens.pop()
                if char != SYM_MAP[last_open]:
                    return None
            else:
                return None
    return recent_opens

def complete_str(unclosed_opens):
    return ''.join((SYM_MAP[char] for char in reversed(unclosed_opens)))

def str_score(complete_string):
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    score = 0
    for char in complete_string:
        score *= 5
        score += score_map[char]
    return score

def part_one(lines):
    failing_chars = [first_failing_char(line) for line in lines]
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        None: 0,
    }
    print(sum([scores[i] for i in failing_chars]))

def part_two(lines):
    incomplete_lines = filter(lambda x: x, map(lambda line: incomplete_opens(line), lines))
    complete_strings = map(lambda x: complete_str(x), incomplete_lines)
    scores = list(map(lambda x: str_score(x), complete_strings))
    middle_score = sorted(scores)[len(scores) // 2]
    print(middle_score)


def main():
    lines = parse_input(INPUT_FILE)
    part_two(lines)

if __name__ == '__main__':
    main()