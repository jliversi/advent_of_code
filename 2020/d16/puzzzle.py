with open('input.txt') as f:
    lines = f.read().split('\n\n')
    rules = lines[0].split('\n')
    my_ticket = lines[1].split('\n')[1]
    other_tickets = lines[2].split('\n')[1:]

ranges = dict()
i = 0
for rule in rules:
    str1 = rule.split()[-3]
    str2 = rule.split()[-1]
    str1 = str1.split('-')
    str2 = str2.split('-')
    ranges[i] = []
    ranges[i].append(range(int(str1[0]), int(str1[1]) + 1))
    ranges[i].append(range(int(str2[0]), int(str2[1]) + 1))
    i += 1

NUM_RULES = len(ranges)
    
valid_tickets = []
for ticket in other_tickets:
    valid = True
    for num in ticket.split(','):
        found = False
        num = int(num)
        for r in ranges:
            if num in ranges[r][0]:
                found = True
            elif num in ranges[r][1]:
                found = True
        if not found:
            valid = False
    if valid:
        valid_tickets.append(ticket)

# now we have valid_tickets

poss_idxs = dict()
for i in range(NUM_RULES):
    poss_idxs[i] = list(range(NUM_RULES))



for k in ranges:
    range_pair = ranges[k]
    x, y = range_pair
    for ticket in valid_tickets:
        for i, num in enumerate(ticket.split(',')):
            num = int(num)
            if num not in x and num not in y:
                poss_idxs[k].remove(i)


results = dict()

while len(results) < NUM_RULES:
    to_remove = []
    for k in poss_idxs:
        poss = poss_idxs[k]
        if len(poss) == 1:
            results[k] = poss[0]
            to_remove.append(poss[0])
    
    for k in poss_idxs:
        poss = poss_idxs[k]
        for el in to_remove:
            if el in poss:
                poss.remove(el)

print(results)
my_ticket = my_ticket.split(',')
total = 1
for i in range(6):
    idx = results[i]
    my_val = int(my_ticket[idx])
    total *= my_val

print(total)