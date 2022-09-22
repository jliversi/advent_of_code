with open('input.txt') as f:
    INPUT = [x.split(' ') for x in f.readlines()]

# PART 1
# X = 0
# DEPTH = 0 

# for el in INPUT:
#     dir, amt = el
#     amt = int(amt)
#     if dir == 'up':
#         DEPTH -= amt
#     elif dir == 'down':
#         DEPTH += amt
#     elif dir == 'forward':
#         X += amt
    
# print(X * DEPTH)

# PART 2
X = 0
DEPTH = 0 
AIM = 0

for el in INPUT:
    dir, amt = el
    amt = int(amt)
    if dir == 'down':
        AIM += amt
    elif dir == 'up':
        AIM -= amt
    elif dir == 'forward':
        X += amt
        DEPTH += amt * AIM
    
print(X * DEPTH)


