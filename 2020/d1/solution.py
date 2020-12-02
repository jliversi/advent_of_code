inputs = []

with open('input.txt', 'r') as f:
    for l in f:
        inputs.append(int(l))


for el1 in inputs:
    for el2 in inputs:
        if (el1 + el2) == 2020:
            print("solution 1")
            print(el1 * el2)


for el1 in inputs:
    for el2 in inputs:
        for el3 in inputs:
            if (el1 + el2 + el3) == 2020:
                print("solution 2")
                print([el1, el2, el3])
                print(el1 * el2 * el3)
