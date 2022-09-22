with open('o_input.txt') as f:
    INPUT = [x.strip() for x in f.readlines()]

def most_common_at(num_list, idx):
    zero_count = 0
    one_count = 0
    for num in num_list:
        if num[idx] == '0':
            zero_count += 1
        else:
            one_count += 1
    if one_count > zero_count:
        return '1'
    elif zero_count > one_count:
        return '0'
    else:
        return 'equal'

def least_common_at(num_list, idx):
    zero_count = 0
    one_count = 0
    for num in num_list:
        if num[idx] == '0':
            zero_count += 1
        else:
            one_count += 1
    if one_count > zero_count:
        return '0'
    elif zero_count > one_count:
        return '1'
    else:
        return 'equal'

# str_len = len(INPUT[0])
# gamma = ''
# epsilon = ''
# for i in range(str_len):
#     gamma += most_common_at(INPUT, i)


# for c in gamma:
#     if c == '0':
#         epsilon += '1'
#     else:
#         epsilon += '0'

# PART 1
# gamma_dec = int(gamma,2)
# epsilon_dec = int(epsilon,2)
# print(gamma_dec * epsilon_dec)

def find_ox(num_list):
    idx = 0
    while len(num_list) > 1:
        rel_bit = most_common_at(num_list, idx)
        if rel_bit == 'equal': rel_bit = '1'
        num_list = list(filter(lambda x: x[idx] == rel_bit, num_list))
        idx += 1
    return num_list[0]

def find_co(num_list):
    idx = 0
    while len(num_list) > 1:
        rel_bit = least_common_at(num_list, idx)
        if rel_bit == 'equal': rel_bit = '0'
        num_list = list(filter(lambda x: x[idx] == rel_bit, num_list))
        idx += 1
    return num_list[0]

ox = find_ox(INPUT)
co = find_co(INPUT)
ox_dec = int(ox,2)
co_dec = int(co,2)
print(ox)
print(ox_dec)
print(co)
print(co_dec)
print(ox_dec * co_dec)