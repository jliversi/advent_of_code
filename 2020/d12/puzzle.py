from itertools import cycle

inputs = []

with open('input.txt','r') as f:
    for l in f:
        inputs.append((l[0],int(l[1:])))


waypoint = [10,1]
N = [0,1]
E = [1,0]
S = [0,-1]
W = [-1,0]

pos = [0,0]

for instruction in inputs:
    way, amt = instruction
    if way == 'N':
        waypoint[1] += amt
    elif way == 'E':
        waypoint[0] += amt 
    elif way == 'S':
        waypoint[1] -= amt 
    elif way == 'W':
        waypoint[0] -= amt
    elif way == 'F':
        pos[0] += (waypoint[0] * amt) 
        pos[1] += (waypoint[1] * amt)
    else:
        num_turns = int(amt/90)
        if way == 'L':
            num_turns = 360 - num_turns
        for i in range(num_turns):
            waypoint = [waypoint[1], -waypoint[0]]


x, y = pos
x = abs(x)
y = abs(y)
print(x+y)




# PART 1
# forward = [1,0]
# dir_cycle = cycle([S,W,N,E])

# pos = [0,0]
# for instruction in inputs:
#     way, amt = instruction
#     if way == 'N':
#         pos[0] += (N[0] * amt) 
#         pos[1] += (N[1] * amt) 
#     elif way == 'E':
#         pos[0] += (E[0] * amt) 
#         pos[1] += (E[1] * amt) 
#     elif way == 'S':
#         pos[0] += (S[0] * amt) 
#         pos[1] += (S[1] * amt) 
#     elif way == 'W':
#         pos[0] += (W[0] * amt) 
#         pos[1] += (W[1] * amt)
#     elif way == 'F':
#         pos[0] += (forward[0] * amt) 
#         pos[1] += (forward[1] * amt)
#     else:
#         num_turns = int(amt/90)
#         if way == 'L':
#             num_turns = 360 - num_turns
#         for i in range(num_turns):
#             forward = next(dir_cycle)

# x, y = pos
# x = abs(x)
# y = abs(y)
# print(x+y)