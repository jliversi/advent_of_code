from intcode import IntcodeComputer

with open('input.txt') as f:
    INPUT = [int(x) for x in f.read().split(',')]


solved = False
result = None
comp = IntcodeComputer(INPUT)
for x in range(100):
    if solved: break
    for y in range(100):
        if solved: break

        comp.alterInput(x,y)
        output = comp.run()
        if output == 19690720:
            solved = True
            result = (x,y)
        comp.refresh()

print(result)

print(100 * result[0] + result[1])

