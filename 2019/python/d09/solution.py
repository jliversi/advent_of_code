from intcode import IntcodeComputer

with open('input.txt') as f:
    INPUT = f.read()
    # INPUT = {idx: int(x) for idx, x in enumerate(f.read().split(','))}

# INPUT = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
# INPUT = '1102,34915192,34915192,7,4,7,99,0'
# INPUT = {idx: int(x) for idx, x in enumerate('104,1125899906842624,99'.split(','))}


comp = IntcodeComputer(INPUT, [2])
output = comp.run()
