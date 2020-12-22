INPUTS = []

with open('input.txt') as f:
    for l in f:
        ingredients_raw, allergins_raw = l.split('(')
        pair = (ingredients_raw.split(), allergins_raw.replace('\n', '').split()[1:] )
        INPUTS.append(pair)

ALL_ALLERGINS = dict()
ALL_INGREDIENTS = dict()

for idx, food in enumerate(INPUTS):
    ingredients, allergins = food
    for ingredient in ingredients:
        if ingredient not in ALL_INGREDIENTS:
            ALL_INGREDIENTS[ingredient] = []
        ALL_INGREDIENTS[ingredient].append(idx)
    for allergin in allergins:
        if allergin not in ALL_ALLERGINS:
            ALL_ALLERGINS[allergin] = []
        ALL_ALLERGINS[allergin].append(idx)

POSS_NAMES_FOR_ALLERGIN = dict()

for a in ALL_ALLERGINS:
    current_set = None
    for idx in ALL_ALLERGINS[a]:
        if not current_set:
            current_set = INPUTS[idx][0]
        else:
            current_set = [x for x in current_set if x in INPUTS[idx][0]]
    POSS_NAMES_FOR_ALLERGIN[a] = current_set

RESULTS = dict()
total_allergins = len(ALL_ALLERGINS)
while len(RESULTS) < total_allergins:
    for k in POSS_NAMES_FOR_ALLERGIN:
        posses = POSS_NAMES_FOR_ALLERGIN[k]
        if len(posses) == 1:
            name = posses[0]
            RESULTS[k] = name
            for k2 in POSS_NAMES_FOR_ALLERGIN:
                if name in POSS_NAMES_FOR_ALLERGIN[k2]:
                    POSS_NAMES_FOR_ALLERGIN[k2].remove(name)

alpha_allergin_arr = sorted(list(RESULTS))
FINAL_STRING = ','.join([RESULTS[x] for x in alpha_allergin_arr])


print(FINAL_STRING)


# PART 1 ANSWERS
# COULD_BE_ALLERGIN = set()
# for a in POSS_NAMES_FOR_ALLERGIN:
#     for el in POSS_NAMES_FOR_ALLERGIN[a]:
#         COULD_BE_ALLERGIN.add(el)

# NO_ALLERGIN_INGREDIENTS = set()
# for i in ALL_INGREDIENTS:
#     if i not in COULD_BE_ALLERGIN:
#         NO_ALLERGIN_INGREDIENTS.add(i)

# total = 0
# for i in NO_ALLERGIN_INGREDIENTS:
#     total += len(ALL_INGREDIENTS[i])

# print(total)