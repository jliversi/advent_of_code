from intcode import IntcodeComputer

with open('input.txt') as f:
    INPUT = [int(x) for x in f.read().split(',')]


comp = IntcodeComputer(INPUT)
comp.run()