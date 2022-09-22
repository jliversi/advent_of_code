inputs = []
with open('input.txt', 'r') as f:
  for l in f:
    inputs.append(l.replace('\n',''))

def has_double_pair(string):
    for i in range(len(string) - 1):
        substr = string[i:i+2]
        if substr in string.replace(substr, '', 1):
            return True
    return False

def has_split_double(string):
    for i, char in enumerate(string):
        if i == len(string) - 2:
            return False
        elif char == string[i + 2]:
            return True

def is_nice_string(string):
    return has_double_pair(string) and has_split_double(string)

NICE_COUNT = 0
for s in inputs:
    if is_nice_string(s):
        NICE_COUNT += 1

print(NICE_COUNT)


# Part 1

# VOWELS = set('aeiou')
# BAD_STRINGS = ['ab', 'cd', 'pq', 'xy']

# def has_double(string):
#     for i, char in enumerate(string):
#         if i == len(string) - 1:
#             return False
#         elif char == string[i + 1]:
#             return True

# def has_three_vowels(string):
#     v_count = 0
#     for char in string:
#         if char in VOWELS:
#             v_count += 1
#         if v_count >= 3:
#             return True
#     return False 

# def has_no_bad(string):
#     for bs in BAD_STRINGS:
#         if bs in string:
#             return False
#     return True

# def is_nice_string(string):
#     return has_no_bad(string) and has_three_vowels(string) and has_double(string)