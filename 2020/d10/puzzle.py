inputs = [0]

with open('input.txt','r') as f:
    for l in f:
        inputs.append(int(l))

inputs.sort()
print("INPUT:")
print(inputs)
print(len(inputs))
print("\n")

max_volts = max(inputs) + 3

def num_choices(i):
    el = inputs[i]
    result = 0
    for x in range(3):
        if (i + x + 1) >= len(inputs):
            return result 


        other = inputs[i + x + 1]
        if (other - el) > 3:
            return result
        else:
            result += 1
    return result 

choices = [] 
for i, adap in enumerate(inputs):
    if i == len(inputs) - 1:
        break
    choices.append(num_choices(i))

for i, el in enumerate(choices):
    if i == 0 or i == (len(choices) - 1):
        continue
    elif el == 1 and (choices[i - 1] == 2 or choices[i - 1] == 3):
        choices[i] = "BREAK"


choices = list(filter(lambda x: x != 1, choices))
print(choices)

total = 1
choices_revised = []
sub_choices = []
for el in choices:
    if el == 'BREAK':
        choices_revised.append(sub_choices)
        sub_choices = []
    else:
        sub_choices.append(el)

if len(sub_choices) > 0:
    choices_revised.append(sub_choices)
    
a = 0
b = 0
for el in choices_revised:
    if el == [3,3,2]:
        a += 1
    else:
        b += len(el)

print(a)
print(b)


# 1. Generate an array where of num_choices (number of choices of next element from a given element of input). this will leave you with a list of 1s, 2s, and 3s
# 2. Split the list on each set of ones, you'll end up with sets of [3,3,2], [3,2] or [2]
# 3. Count the number of sets of [3,3,2]. This is A
# 4. Count the number of elements in sets that _aren't_ [3,3,2]. This is B 
# 5. (7^A) * (2^B) is the answer

# tried to use 

# num_1s = 0
# num_3s = 0 
# num_unskipables = 0
# unskippables = []
# just_found_3_gap = False 
# for i, el in enumerate(inputs):
#     if i == 0:
#         if el == 1:
#             num_1s += 1
#         elif el == 3:
#             num_3s += 1
#             unskippables.append(el)
#     elif (el - inputs[i - 1]) == 1:
#         just_found_3_gap = False
#         num_1s += 1
#     elif (el - inputs[i - 1]) == 3:
#         num_3s += 1
#         if just_found_3_gap:
#             unskippables.append(el)
#             num_unskipables += 1
#         else:
#             unskippables.append(el)
#             unskippables.append(inputs[i - 1])
#             num_unskipables += 2
#             just_found_3_gap = True
#     else:
#         just_found_3_gap = False

# num_skippable = len(inputs) - num_unskipables
# skippables = []
# for el in inputs:
#     if el not in unskippables:
#         skippables.append(el)



# print('skippables: ')
# print(skippables)

# a = 0
# b = 4
# x = len(skippables)
# print(x)

# term1 = 2**x
# term2 = a*(2**(x-2))
# term3 = b*(2**(x-3))
# result = term1 - term2 - term3
# print(term1, term2, term3)
# print(result)






Megan
Stephen Yim
Ariel

Ara
Galen
Chris Mann

Daniel
Sukhdip
Russel
Juan Sanchez
Derek Chen

