with open('input.txt') as f:
    INPUT = list(map(lambda x: int(x), f.readlines()))

# Part 1
# total = 0
# for i in len(INPUT):
#     if i != 0:
#         if INPUT[i] > INPUT[i - 1]:
#             total += 1

sums = []
for i, el in enumerate(INPUT):
    if i <= len(INPUT) - 3:
        sums.append(sum(INPUT[i:i+3]))

total = 0
for i, el in enumerate(sums):
    if i != 0:
        if el > sums[i - 1]:
            total += 1

print(total)