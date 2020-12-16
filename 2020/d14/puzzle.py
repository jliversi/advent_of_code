from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


with open('input.txt') as f:
    inputs = [l.replace('\n','') for l in f]


memory = dict()

def poss_addresses(num, bit_string):
    results = []
    or_num = int(bit_string.replace('X','0'), 2)
    num |= or_num
    num = '{:036b}'.format(num)
    x_idxs = []
    for i in range(len(bit_string)):
        if bit_string[i] == 'X':
            x_idxs.append(i)
    for el in powerset(x_idxs):
        new_str = ''
        for i, char in enumerate(num):
            if i not in x_idxs:
                new_str += char
            elif i in el:
                new_str += '1'
            else:
                new_str += '0'
        results.append(int(new_str, 2))
    return results

        



for l in inputs:
    r_typ, _, num = l.split()
    if r_typ == 'mask':
        mask = num
    else:
        mem_address = int(r_typ[4:-1])
        poss = poss_addresses(mem_address, mask)
        for el in poss:
            memory[el] = int(num)

total = 0
for k in memory:
    total += memory[k]

print(total)
print(len(memory))





# PART 1
# for l in inputs: 
#     r_typ, _, num = l.split()
#     if r_typ == 'mask':
#         and_m = ''
#         or_m = ''
#         for char in num:
#             if char == '1':
#                 and_m += '1' 
#                 or_m += '1' 
#             elif char == '0':
#                 and_m += '0' 
#                 or_m += '0' 
#             else:
#                 and_m += '1' 
#                 or_m += '0'
#     else:
#         mem_address = int(r_typ[4:-1])
#         val = int(num) & int(and_m, 2) | int(or_m,2)
#         memory[mem_address] = val

# total = 0
# for k in memory:
#     total += memory[k]

# print(total)
